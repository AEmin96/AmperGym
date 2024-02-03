from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        # Custom logic to return the redirect URL
        return super(MyAccountAdapter, self).get_login_redirect_url(request)
