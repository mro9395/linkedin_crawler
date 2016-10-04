#Inspired from https://github.com/ozgur/python-linkedin
#LinkedIn app configuration
#https://localhost:8080/auth/linkedin/callback
#Insert key and secret
KEY="KEY"
SECRET="SECRET"

# Credentials you get from registering a new application
client_id = KEY
client_secret = SECRET

# OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'

from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import linkedin_compliance_fix

linkedin = OAuth2Session(client_id, redirect_uri='https://localhost:8080/auth/linkedin/callback')
linkedin = linkedin_compliance_fix(linkedin)

# Redirect user to LinkedIn for authorization
authorization_url, state = linkedin.authorization_url(authorization_base_url)
print ('Please go here and authorize,' + authorization_url)

# Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')

# Fetch the access token
linkedin.fetch_token(token_url, client_secret=client_secret,authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
#r = linkedin.get('https://api.linkedin.com/v1/people/~?format=json')
#print (r.content)

#r = linkedin.get('https://api.linkedin.com/v1/company-search:(companies:(id,name,universal-name,website-url))?keywords=microsoft')
#print (r.content)

#r = linkedin.get('https://api.linkedin.com/v1/people/id=hldNKx_45J')
#print (r.content)

user_continue ="Y"

while user_continue == "Y":
    call = input('Select your call (Profile, By ID, URL)')

    if  call == "Profile":
        r = linkedin.get('https://api.linkedin.com/v1/people/id=hldNKx_45J:(id,first-name,last-name,headline,industry,location,specialties,summary,positions,num-connections)?format=json')

    elif call == "By ID":
        id_requested = input("ID:")
        r = linkedin.get('https://api.linkedin.com/v1/people/id=' + id_requested + ':(id,first-name,last-name,headline,three-current-positions,industry,location,specialties,summary,positions,num-connections)?format=json')

    elif call == "URL":
        public_url = input("URL:")
        r = linkedin.get('https://api.linkedin.com/v1/people/url=https%3A%2F%2Fwww.linkedin.com%2Fin%2F' + public_url)

    print(r.content)

    user_continue = input('¿Otra consulta? (Y/N)')

print("exit code 0")


