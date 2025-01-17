import csv
import time
import dns.resolver
from colorama import Fore, init
import sys

init(autoreset=True)


def read_list(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"未找到文件 {file_path}")
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
        return "ERROR"


def generate_table(dns_servers, websites, output_file):
    results = []

    for dns in dns_servers:
        sys.stdout.write(Fore.YELLOW + f"正在测试 DNS 服务器 {dns} ...\r")
        sys.stdout.flush()
        row = [dns]
        for site in websites:
            result = test_dns(dns, site)
            row.append(result)
        results.append(row)
        sys.stdout.write(" " * 50 + "\r")
        sys.stdout.flush()
        print(Fore.GREEN + f"DNS 服务器 {dns} 测试完成")

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        header = [""] + dns_servers
        writer.writerow(header)

        for i, site in enumerate(websites):
            row = [site] + [results[j][i + 1] for j in range(len(dns_servers))]
            writer.writerow(row)

    print(Fore.CYAN + f"测试结果已保存到 {output_file}")


if __name__ == "__main__":
    dns_file = "server.txt"
    website_file = "website.txt"
    output_csv = "results.csv"

    dns_servers = read_list(dns_file)
    websites = read_list(website_file)

    if dns_servers and websites:
        generate_table(dns_servers, websites, output_csv)
    else:
        print(Fore.RED + "请确保 {dns_file} 和 {website_file} 均存在且不为空！")
