import pickledb
import os
import hashlib


values = ""

db_dir = "/python_programs/Decisio/userData"
db_path = os.path.join(db_dir, "userData.db")
os.makedirs(db_dir, exist_ok=True)
db = pickledb.load(db_path, True)

# Function to hash a password
def hash_password(password):
    # Using SHA-256 for hashing
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()


def create_user(username, password):
    if username not in db.getall():
        hashed_password = hash_password(password)
        db.set(username, {'password': hashed_password,
                           'q_one' : [],
                           'q_two': [],
                           'q_three': [],
                           'q_four': [],
                           'q_five': [],
            
                          })
        
        
    else: 
        print("User Already Exists!")

def login_user(username, password):
    if db.exists(username):
        
        
        stored_password = db.get(username)['password']
        entered_password = hash_password(password)

        if stored_password == entered_password:
            
            return True
        else: 
            
            return False
    else: 
        print("Incorrect Username")
        
    




    
    
def get_ans(inp):
    if inp == 1:
        score = 20
        return score
    if inp == 2:
        score = 40
        return score
    if inp == 3:
        score = 60
        return score
    if inp == 4:
        score = 80
        return score
    if inp == 5:
        score = 100
        return score
    

# 5 Values : 


# Ask multiple questions to evalute personal values (1-5 Scale)
# Multiply by 20 (20, 40, 60, 80, 100)
# Store values by question number (q_one : 20)
