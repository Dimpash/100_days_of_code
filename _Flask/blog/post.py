import requests


class Post:

    def __init__(self):
        response = requests.get('https://api.npoint.io/61ebc1048f18837f4720')
        self.blog_posts = response.json()
        self.current_post = self.blog_posts[0]

    def get_data(self, post_id):
        for item in self.blog_posts:
            if int(item['id']) == post_id:
                self.current_post = item


