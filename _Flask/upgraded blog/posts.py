import requests


# class BlogPosts:
#
#     def __init__(self):
#         response = requests.get('https://api.npoint.io/8346e7ee0bb9bcfaedac')
#         self.blog_posts = response.json()
#         # print(self.blog_posts)

class Posts:

    def __init__(self):
        response = requests.get('https://api.npoint.io/8346e7ee0bb9bcfaedac')
        self.blog_posts = response.json()
        self.current_post = self.blog_posts[0]

    def get_data(self, post_id):
        for item in self.blog_posts:
            if int(item['id']) == post_id:
                self.current_post = item


