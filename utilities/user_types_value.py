# returns user type
class user_types:
    @property
    def admin(self):
        return ('admin_user')

    @property
    def merchant(self):
        return ('merchant_user')
