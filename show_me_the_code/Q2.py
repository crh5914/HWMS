#生成200个优惠券
import string,random
import redis
items = string.ascii_letters+string.digits

def getRandom():
	return ''.join(random.sample(items,4))
def concatenate(group):
	return '-'.join([getRandom() for i in range(group)])
def generate(n):
	return [concatenate(4) for i in range(n)]
def saveToRedis(codes):
	cli = redis.StrictRedis(host='127.0.0.1',port='6379')
	cli.set('codes',codes)

if __name__ == '__main__':
	codes = generate(200)
	print(codes)
	saveToRedis(codes)