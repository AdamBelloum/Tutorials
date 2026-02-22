from fastapi import FastAPI, HTTPException
import schemas
import jwt
import json
import os

app = FastAPI()

USERS_FILE = "./user_data/users.json"

if not os.path.exists('user_data'):
    os.makedirs('user_data')

USERS_FILE = './user_data/users.json'

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, "w") as f:
        json.dump([], f)

def read_users():
    """Read the users from the JSON file"""
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def write_users(new_user):
    """Add a new user to the JSON file"""
    with open(USERS_FILE, "r+") as f:
        # read the existing users from the file
        users = json.load(f)

        # append the new user to the list of users
        users.append(new_user)

        # move the file pointer to the beginning of the file
        f.seek(0)

        # write the updated list of users back to the file
        json.dump(users, f, indent=4)

        # truncate the remaining content (in case the new data is shorter than the previous content)
        f.truncate()


def update_user(username, new_data):
    with open(USERS_FILE, "r") as f:
        users = json.load(f)

    # Find the user with the specified username
    for user in users:
        if user["username"] == username:
            # Update the user's data
            user.update(new_data)

            # Write the updated data to the file
            with open(USERS_FILE, "w") as f:
                json.dump(users, f)

            return True

    # If the specified username is not found, return False
    return False


@app.post("/users", status_code=201)
async def create_user(request: schemas.User):
    users = read_users()
    if users is not None:
        usernames = []
        for user in users:
            # print(user)
            usernames.append(user["username"])
            print(usernames)
        if request.username in usernames:
            # If the username already exists, raise an exception
            usernames = []
            raise HTTPException(
                status_code=409, detail="duplicate")
        else:
            user = {"username": request.username,
                    "password": request.password, "token": None}
            write_users(user)
            usernames = []
            return {"message": "User created successfully"}
    else:
        user = {"username": request.username,
                "password": request.password, "token": None}
        write_users(user)
        usernames = []
        return {"message": "User created successfully"}


@app.post("/users/login")
async def login_user(request: schemas.User):
    # Load the existing users
    users = read_users()
    # print(users)
    # iterate a list of dictionaries and return the index and the dictionary
    for user in users:
        if user["username"] == request.username and user["password"] == request.password:
            token = jwt.generate({"username": user["username"]})
            user["token"] = token

            # Save the updated users
            update_user(user["username"], user)

            return {"token": token}
    raise HTTPException(
        status_code=403, detail="forbidden")


@app.put("/users")
async def update_user_password(request: schemas.UserNewPassword):
    users = read_users()
    # Check if the username and password are correct
    for user in users:
        if user["username"] == request.username and user["password"] == request.password:
            #user["password"] = request.new_password
            user = {"username": request.username,
                    "password": request.new_password, "token": None}
            update_user(user["username"], user)
            return {"message": "Password updated successfully"}
    raise HTTPException(
        status_code=403, detail="forbidden")

# validate the token


@app.post("/users/validate")
async def validate_token(request: schemas.Token):
    try:
        users = read_users()
        if request.token in [user["token"] for user in users]:
            tokenData = jwt.decode(request.token)
            token_str = tokenData.decode("utf-8")
            token_data = json.loads(token_str)
            print(tokenData)
            return {"message": "Token is valid", "username": token_data["username"]}
        raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.InvalidToken:
        raise HTTPException(status_code=401, detail="Invalid token")
