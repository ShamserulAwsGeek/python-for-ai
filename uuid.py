# UUID = Universally Unique Identifier
# generates a random, globally unique ID — used whenever you need to identify something (user, file, request, session) without clashing with anyone else's

from uuid import uuid4

unique_id = uuid4()
print(unique_id)        # 550e8400-e29b-41d4-a716-446655440000
print(str(unique_id))   # convert to string
print(type(unique_id))  # <class 'uuid.UUID'>

-----------------------------------
------------------------------------
#Database record:
from uuid import uuid4

class User:
    def __init__(self, name):
        self.id = uuid4()        # unique ID for every user
        self.name = name

u1 = User("Ram")
u2 = User("Sam")

print(u1.id)   # 3d6f-... 
print(u2.id)   # 9b2a-...   completely different

-------------------------------
--------------------------------
#Files names : avoid overwriting:
from uuid import uuid4

def save_file(content):
    filename = f"{uuid4()}.txt"    # unique name every time
    with open(filename, "w") as f:
        f.write(content)
    return filename

# Every call creates a unique file
save_file("hello")   # 3a9f2b....txt
save_file("world")   # 8c4d1e....txt  never overwrites first



--------------------------------
---------------------------------
#Session/Token generation:
from uuid import uuid4

def create_session(user):
    session_token = str(uuid4())   # unique token per login
    return session_token

token = create_session("Ram")
print(token)   # use this as login session key
---------------------------
--------------------------
#Request Tracking:
from uuid import uuid4

def handle_request(data):
    request_id = uuid4()           # track each request uniquely
    print(f"Request {request_id} started")
    # process...
    print(f"Request {request_id} completed")


