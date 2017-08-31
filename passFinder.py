# the lib which we use to make the hashes
import hashlib

# the response
print ("Enter the response! in double quotation please ")
response = input()
# the nonce
print ("Enter the nonce! in double quotation please ")
nonce = str(input())
# the nonce counter
print ("Enter the nonce counter! in double quotation please ")
nc = str(input())
# the QOP
print ("Enter the QOP! in double quotation please")
qop = str(input())
# the client nonce
print ("Enter the client nonce! in double quotation please")
cnonce = str(input())
# the method
print ("Enter the client Method! in double quotation please")
method = str(input())
# the url
print ("Enter the client URL! in double quotation please")
url = str(input())
# th user name
print ("Enter the client user name! in double quotation please")
username = str(input())
# the realm
print ("Enter the realm! in double quotation please")
realm = str(input())
# make hash2
hash2=hashlib.md5(method+':'+url).hexdigest()

# open the possible passwords  file
file = open("passwordsList.txt","r")

# initiate the pass variable
ourPassword = ''


# def to try all the passes
def passFinder(password):
    # make hash1
    hash1 = hashlib.md5(username + ":" + realm + ":" + password).hexdigest()
    # compair the responses
    if response == hashlib.md5(hash1 + ':' + nonce + ':' + nc + ':' + cnonce + ':' + qop + ':' + hash2).hexdigest() :
        return password

# take line by line from the file to check if it's the password or not
for line in file:
    ourPassword =  passFinder(line)

if ourPassword == None:
    print ("Sorry can't find it")
else:
    # print the one
    print ("this is the one we want ")
    print (ourPassword)
