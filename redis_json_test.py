import redis

# Establishing the connection with Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# To Insert JSON in Redis
json_message = {"Name":"First","Body":"first message body"}
list_key = "json_list"
redis_client.lpush(list_key,str(json_message))


# To Read from Redis
redis_pop = redis_client.lpop(list_key)
json_message_from_redis = eval(redis_pop)
print(json_message_from_redis["Body"])

# Closing the connection
redis_client.close()
