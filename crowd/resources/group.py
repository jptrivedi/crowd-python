from crowd.base import Crowd

class GroupResource(Crowd):

    def __init__(self, app_host, user, password):
        super(GroupResource, self).__init__(app_host, user, password)
        self.app_url = "%s/user" % self.app_url

    def get_group(self, groupname):
        params = {"groupname":groupname}
        return super(GroupResource, self).get(params)

    def delete_group(self, groupname):
        params = {"groupname":groupname}
        return super(GroupResource, self).delete(params)
