import instaloader

L = instaloader.Instaloader()
L.interactive_login("user")     # Melhor opção caso seu perfil possua MFA

# Aqui definimos qual o usuário que iremos utilizar
profile = instaloader.Profile.from_username(L.context, "User")
follow_list = []
for followee in profile.get_followers():
    username = followee.username
    follow_list.append(username)
    
following_list = []
for followee in profile.get_followees():
    username = followee.username
    following_list.append(username)
    
# Listar usuários que você segue, mas não seguem você
list(set(following_list) - set(follow_list))

# Listar que te seguem, mas você não segue que você segue, mas não seguem você
list(set(follow_list) - set(following_list))
