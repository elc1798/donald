# Donald - Medium Clone
----------------

## Pages
- `/` list all posts
- `/@username` list posts for one user
- `/@username/post-slug` show individual post
- `/login` Login
- `/signup` Signup
- `/new` Create a new post

## API
- `GET /` - Return List of all posts
- `POST /new` - Create a new post
- `POST /login` - Login in a user with session
- `POST /signup` - Signup user and login with session
- `GET /@username` - Return List of posts from one user
- `GET /@username/post-slug/` - Return post
- `POST /@username/post-slug/comments` - Create new comment

## Team Members
- Chris Grant (Team Leader)
- Helen Li (UX)
- David Song (Backend)
- Tony Li (Middleware)

## Setup
`pip install flask`
`pip install python-slugify`

## Run
`python app.py`
