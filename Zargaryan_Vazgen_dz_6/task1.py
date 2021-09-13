with open ('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    ips = []
    gets = []
    downloads = []
    for _ in f:
        ips.append(_.split()[0])
        gets.append(_.replace('"',' ').split()[5])
        downloads.append(_.split()[6])

result = tuple(zip(ips,gets,downloads))

for i in result:
    print(i)




