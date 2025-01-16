import csv
import time
import dns.resolver


def read_list(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File {file_path} not found!")
        return []


def test_dns(dns_server, website, num_tests=3):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    times = []
    for i in range(1, num_tests + 1):
        try:
            start_time = time.time()
            resolver.resolve(website)
            elapsed_time = (time.time() - start_time) * 1000
            times.append(elapsed_time)
        except dns.resolver.Timeout:
            times.append(None)
        except Exception:
            times.append(None)

    valid_times = [t for t in times if t is not None]
    if valid_times:
        return round(sum(valid_times) / len(valid_times))
    else:
        return "Timeout/Error"


def generate_table(dns_servers, websites, output_file):
    results = []

    for dns in dns_servers:
        row = [dns]
        for site in websites:
            result = test_dns(dns, site)
            row.append(result)
        results.append(row)
        print(f"DNS server {dns} tests complete")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        header = [""] + dns_servers
        writer.writerow(header)

        for i, site in enumerate(websites):
            row = [site] + [results[j][i + 1] for j in range(len(dns_servers))]
            writer.writerow(row)

    print(f"Test results saved to {output_file}")


if __name__ == "__main__":
    dns_file = "server.txt"
    website_file = "website.txt"
    output_csv = "dns_test_results.csv"

    dns_servers = read_list(dns_file)
    websites = read_list(website_file)

    if dns_servers and websites:
        generate_table(dns_servers, websites, output_csv)
    else:
        print(
            "Please ensure that both DNS server list and website list files exist and are not empty!"
        )
