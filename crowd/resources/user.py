from crowd.base import Crowd

class UserResource(Crowd):

    def __init__(self, app_host, user, password):
        super(UserResource, self).__init__(app_host, user, password)
        self.app_url = "%s/user" % self.app_url

    def get_user(self, username):
        params = {"username":username}
        return super(UserResource, self).get(params)

    def delete_user(self, username):
        params = {"username":username}
        return super(UserResource, self).delete(params)

    def exists(self, username):
        response = self.get_user(username)
        return "USER_NOT_FOUND" not in response
