import redis
import json
import pymongo


pool = redis.ConnectionPool()
redis_cli = redis.Redis(connection_pool=pool)
mongo_cli = pymongo.MongoClient(host='127.0.0.1', port=27017)
sheet = mongo_cli.hsw.hsw_items


def main():
    offset = 0
    while True:
        # FIFO模式为 blpop，LIFO模式为 brpop，获取键值
        source, data = redis_cli.blpop(['hsw_spider:items'])
        item = json.loads(data.decode('utf-8'))
        sheet.insert(item)
        offset += 1
        print(offset)
        try:
            print("processing {}".format(item))
        except KeyError:
            print("error processing {}".format(item))


if __name__ == '__main__':
    main()

