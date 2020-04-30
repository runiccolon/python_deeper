from collections import ChainMap

# 有一个注意点就是当对ChainMap进行修改的时候总是只会对第一个字典进行修改
a = {"x": 1, "z": 3}
b = {"y": 2, "z": 4}
c = ChainMap(a, b)
print(c)
print("x: {}, y: {}, z: {}".format(c["x"], c["y"], c["z"]))
