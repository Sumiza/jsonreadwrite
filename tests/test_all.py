

from jsonreadwrite import JsonReadWrite

testlist = ["test1", "test2", "test3"]
testdict = {"test1": "test1", "test2": "test2", "test3": "test3"}
testint = 1
testfloat = 1.1
testbool = True
testnone = None
testblank = ""

test = JsonReadWrite("test.json",allowempty=True)

test.set("testlist", testlist)
test.set("testdict", testdict)
test.set("testint", testint)
test.set("testfloat", testfloat)
test.set("testbool", testbool)
test.set("testnone", testnone)
test.set("testblank", testblank)

assert test.get("testlist") == testlist
assert test.get("testdict") == testdict
assert test.get("testint") == testint
assert test.get("testfloat") == testfloat
assert test.get("testbool") == testbool
assert test.get("testnone") == testnone
assert test.get("testblank") == testblank