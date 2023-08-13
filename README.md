CMS Application API Documentation
User Table
Create User
Endpoint: POST /api/users
Description: Add a new user to the Auther table.
Request Body:
  {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "secretpassword",
  }

Read User :
  Endpoint: GET /users/{userId}
  Description: Retrieve information about a specific user.
  Response: The user object.
Update User :
  Endpoint: PUT /users/{userId}
  Description: Update details of a specific user.
  Request Body: Updated user details.
  Response: The updated user object.
Delete User :
  Endpoint: DELETE /users/{userId}
  Description: Delete a specific user.
  Response: A success message.


Post/Blog Endpoints
Create Post/Blog
Endpoint: POST /posts
Description: Create a new post/blog.
Request Body:
  {
    "title": "My Blog Post",
    "description": "An interesting blog post",
    "content": "Lorem ipsum dolor sit amet...",
  }

Read Post/Blog :
  Endpoint: GET /posts/{postId}
  Description: Retrieve information about a specific post/blog.
  Response: The post object with the number of likes.
Update Post/Blog :
  Endpoint: PUT /posts/{postId}
  Description: Update details of a specific post/blog.
  Request Body: Updated post details.
  Response: The updated post object.
Delete Post/Blog
  Endpoint: DELETE /posts/{postId}
  Description: Delete a specific post/blog.
  Response: A success message.


Like Endpoints
Create Like
Endpoint: POST /likes
Description: Add a like to a specific post/blog.
Request Body:
  {
    "postId": "post_id_here"
  }

Read Like :
  Endpoint: GET /likes/{likeId}
  Description: Retrieve information about a specific like.
  Response: The like object.
Update Like :
  Endpoint: PUT /likes/{likeId}
  Description: Update details of a specific like.
  Request Body: Updated like details.
  Response: The updated like object.
Delete Like :
  Endpoint: DELETE /likes/{likeId}
  Description: Delete a specific like.
  Response: A success message.
