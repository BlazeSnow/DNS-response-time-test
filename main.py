import csv
import time
import dns.resolver


def read_list(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到！")
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
        return "超时/错误"


def generate_table(dns_servers, websites, output_file):
    results = []

    for dns in dns_servers:
        row = [dns]
        for site in websites:
            result = test_dns(dns, site)
            row.append(result)
        results.append(row)
        print(f"DNS 服务器 {dns} 测试完成")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        header = [""] + dns_servers
        writer.writerow(header)

        for i, site in enumerate(websites):
            row = [site] + [results[j][i + 1] for j in range(len(dns_servers))]
            writer.writerow(row)

    print(f"测试结果已保存到 {output_file}")


if __name__ == "__main__":
    dns_file = "server.txt"
    website_file = "website.txt"
    output_csv = "results.csv"

    dns_servers = read_list(dns_file)
    websites = read_list(website_file)

    if dns_servers and websites:
        generate_table(dns_servers, websites, output_csv)
    else:
        print("请确保 DNS 服务器列表和网站列表文件均存在且不为空！")
