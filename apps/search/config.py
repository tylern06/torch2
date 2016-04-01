from authomatic.providers import oauth2, oauth1, openid

CONFIG = {
    
    'tw': { # Your internal provider name
        
        # Provider class
        'class_': oauth1.Twitter,
        
        # Twitter is an AuthorizationProvider so we need to set several other properties too:
        'consumer_key': 'jMR1XlDApdYtdXPpMtONFbAeK',
        'consumer_secret': 'mEQjS6KVQzttJvG1s1lasAHIR7IXSh6gUEGigctUVvY7uZfBwP',
        # 'request_token' : '715600701322166272-HZIwkDyJ1vxpoyK5L3VkrNseOzjf1xy',
    },
    
    # 'fb': {
           
    #     'class_': oauth2.Facebook,
        
    #     # Facebook is an AuthorizationProvider too.
    #     'consumer_key': '########################',
    #     'consumer_secret': '########################',
        
    #     # But it is also an OAuth 2.0 provider and it needs scope.
    #     'scope': ['user_about_me', 'email', 'publish_stream'],
    # },
    
    'oi': {
           
        # OpenID provider dependent on the python-openid package.
        'class_': openid.OpenID,
    }
}