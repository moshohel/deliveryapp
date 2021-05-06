# Checks user Type
def admin_user(User):
    if(User.user_type == "admin_user"):
        return True

    return False


def merchant_user(User):
    if(User.user_type == "merchant_user"):
        return True

    return False
