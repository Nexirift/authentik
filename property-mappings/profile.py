return {
    # Because authentik only saves the user's full name, and has no concept of first and last names,
    # the full name is used as given name.
    # You can override this behaviour in custom mappings, i.e. `request.user.name.split(" ")`
    "name": request.user.name,
    "given_name": request.user.name,
    "preferred_username": request.user.username,
    "nickname": request.user.username,
    # To ensure compatability with services that try to get "picture".
    "picture": request.user.attributes.get("avatar", "https://auth.nexirift.com/media/user-avatars/default.png"),
    # Nexirift specific features.
    "avatar": request.user.attributes.get("avatar", "https://auth.nexirift.com/media/user-avatars/default.png"),
    "banner": request.user.attributes.get("banner"),
    "background": request.user.attributes.get("background"),
    # groups is not part of the official userinfo schema, but is a quasi-standard
    "groups": [group.name for group in request.user.ak_groups.all()],
}