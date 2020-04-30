from influxdb import influxdb08

client = influxdb08.InfluxDBClient('localhost', 8086, 'root', '', 'test')
print(client.get_list_database())
