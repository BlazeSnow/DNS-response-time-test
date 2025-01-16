import csv
import time
import dns.resolver


def read_list(file_path):
    """从文件中读取列表"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到！")
        return []


def test_dns(dns_server, website):
    """测试 DNS 服务器对某个网站的响应时间"""
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [dns_server]
    try:
        start_time = time.time()
        resolver.resolve(website)
        return round((time.time() - start_time) * 1000)  # 转换为整数的毫秒
    except dns.resolver.Timeout:
        return "超时"
    except Exception as e:
        return f"错误: {e}"


def generate_table(dns_servers, websites, output_file):
    """生成包含测试结果的表格，行和列对调"""
    results = []

    # 先计算所有结果
    for dns in dns_servers:
        row = [dns]
        for site in websites:
            result = test_dns(dns, site)
            row.append(result)
        results.append(row)

    # 写入 CSV，行列对调
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # 写入列头
        header = [""] + dns_servers  # 第一行留白
        writer.writerow(header)

        # 写入数据（网站为行，DNS 为列）
        for i, site in enumerate(websites):
            row = [site] + [results[j][i + 1] for j in range(len(dns_servers))]
            writer.writerow(row)

    print(f"测试结果已保存到 {output_file}")


if __name__ == "__main__":
    dns_file = "server.txt"
    website_file = "website.txt"
    output_csv = "dns_test_results.csv"

    dns_servers = read_list(dns_file)
    websites = read_list(website_file)

    if dns_servers and websites:
        generate_table(dns_servers, websites, output_csv)
    else:
        print("请确保 DNS 服务器列表和网站列表文件均存在且不为空！")
