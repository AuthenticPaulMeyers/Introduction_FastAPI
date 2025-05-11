from fastapi import FastAPI, Response, status, HTTPException

app = FastAPI()


# posts collection
my_posts = [
    {
        "id": 1,
        "title": "favourite food",
        "content": "my favourite food is mostly vegetables with meat"
    },
    {
        "id": 2,
        "title": "girlfriend",
        "content": "i think am still in love with Alice, maybe i am"
    },
    {
        "id": 3,
        "title": "songs",
        "content": "these are my favorite songs"
    }
]


# get post using the id
def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

# get all posts
@app.get("/posts")
def root():
    return {"data": my_posts}

# create post
@app.post("/create_post")
def create_post():
    return {"post": "this is your post"}

# get latest post
@app.get("/posts/latest")
def get_latest_post():
    print(len(my_posts) - 1)
    post = my_posts[len(my_posts) - 1]
    return {"post": post}

# get a single post
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    # catch the error if the file is not found
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"error {status.HTTP_404_NOT_FOUND}. File not found.")
    return {"data": post}

# delete a post
@app.delete("/posts/{id}")
def delete_post(id: int):

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update post
@app.put("/posts/{id}", status_code=status.HTTP_201_CREATED)
def update_post(id: int):
    return {"message": "Post updated."}

