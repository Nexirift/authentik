<p align="center">
<img src="https://raw.githubusercontent.com/Nexirift/.github/main/banner.svg" width="300" />
</p>

# Authentik

A repository to hold configs for the authentication solution we use:
[Authentik](https://goauthentik.io/).

## Policies

### Nexirift-User-Settings-Authorization

The purpose of this policy is to allow users to upload avatars, banners and
backgrounds.

#### Setup

1. Create a new **expression** policy (Customization > Policies):
    - **Name:** nexirift-user-settings-authorization
    - **Expression:** _Copy the contents of this
      [file](https://raw.githubusercontent.com/Nexirift/authentik/main/policies/nexirift-user-settings-authorization.py)_.
2. Create a three new prompts (Flow and Stages > Prompts):
    1. Avatar
        - **Name:** nexirift-user-settings-field-avatar
        - **Field Key:** attributes.avatar
        - **Label:** User Avatar
        - **Type:** File
        - **Order:** 300
    2. Banner
        - **Name:** nexirift-user-settings-field-banner
        - **Field Key:** attributes.banner
        - **Label:** User Banner
        - **Type:** File
        - **Order:** 301
    3. Background
        - **Name:** nexirift-user-settings-field-background
        - **Field Key:** attributes.background
        - **Label:** User Background
        - **Type:** File
        - **Order:** 302
3. Edit `default-user-settings` (Flow and Stages > Stages):
    - Select the fields that we created earlier.
    - Select the validation (expression) policy.

### Nexirift-Enforce-Case-Sensitive-Usernames

The purpose of this policy is to ensure that usernames are case-sensitive.

#### Setup

1. Create a new **expression** policy (Customization > Policies):
    - **Name:** nexirift-enforce-case-sensitive-usernames
    - **Expression:** _Copy the contents of this
      [file](https://raw.githubusercontent.com/Nexirift/authentik/main/policies/nexirift-enforce-case-sensitive-usernames.py)_.
2. Enforce it on all enrollment flows (Flow and Stages > Stages).

## Property Mappings

### Profile

The purpose of this property mapping is to expose picture, avatar, banner, and
backgrounds.

#### Setup

1. Uncheck `Hide managed mappings` (Customization > Property Mappings).
2. Edit `authentik default OAuth Mapping: OpenID 'profile'`:
    - **Expression:** _Copy the contents of this
      [file](https://raw.githubusercontent.com/Nexirift/authentik/main/property-mappings/profile.py)_.

## Social Logins

We use the following social logins:

-   Discord
-   GitHub
-   GitLab
-   Google
-   Patreon
-   Proton via SimpleLogin
-   Reddit
-   Twitch
-   Twitter

### NOTE

Ensure that ALL social logins follow this configuration:

-   **User matching mode:** Use the user's email address, but deny enrollment
    when the email address already exists
-   **Authentication flow:** default-source-authentication

### Proton via SimpleLogin

The purpose of this policy is to allow users to login with their Proton account.

#### Setup

1. Login with a Proton account to SimpleLogin:
   https://simplelogin.com/developers.
2. Create a new developer application:
    - **Name:** Nexirift
    - **Redirect URI:**
      https://auth.nexirift.com/source/oauth/callback/simplelogin/
3. Create a new OpenID OAuth Source:
    - **Name:** Proton via SimpleLogin
    - **Slug:** simplelogin
    - **Consumer key:** _The Client ID from the previous step_
    - **Consumer secret:** _The Client Secret from the previous step_
    - **Authorization URL:** https://app.simplelogin.io/oauth2/authorize
    - **Access token URL:** https://app.simplelogin.io/oauth2/token
    - **Profile URL:** https://app.simplelogin.io/oauth2/userinfo
    - **OIDC Well-Known URL:**
      https://app.simplelogin.io/.well-known/openid-configuration
    - **OIDC JWKS URL:** https://app.simplelogin.io/jwks

## Brand Settings

### Show display name in navigation bar

By default, Authentik will show the username in the navigation bar next to the
profile picture. It would be a better design choice to show the display name
instead of the username.

1. Go to System > Brands and edit the `authentik-default` brand.
2. Show `Other global settings` and put this in `Attributes`:

```yaml
settings:
    navbar:
        userDisplay: name
```

## Credits

Media upload expressions were taken from
[this discussion](https://github.com/goauthentik/authentik/discussions/6824) and
edited to fit our needs.
