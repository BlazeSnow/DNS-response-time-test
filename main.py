import csv
import time
import subprocess


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
    try:
        start_time = time.time()
        subprocess.run(
            ["nslookup", website, dns_server],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5,
        )
        return round((time.time() - start_time) * 1000, 2)  # 转换为毫秒
    except subprocess.TimeoutExpired:
        return "超时"
    except Exception as e:
        return f"错误: {e}"


def generate_table(dns_servers, websites, output_file):
    """生成包含测试结果的表格"""
    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        header = ["DNS服务器\\网站"] + websites
        writer.writerow(header)

        for dns in dns_servers:
            row = [dns]
            for site in websites:
                result = test_dns(dns, site)
                row.append(result)
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
