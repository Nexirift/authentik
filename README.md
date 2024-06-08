<p align="center">
<img src="https://raw.githubusercontent.com/Nexirift/.github/main/banner.svg" width="300" />
</p>

# Authentik

A repository to hold configs for the authentication solution we use:
[Authentik](https://goauthentik.io/).

## Groups

We have the following groups set up in Authentik:

-   Nexirift Staff
    -   **Attributes:**
        `notes: "This is for staff related services, such as Galaxy, etc."`
-   Nexirift Developers
    -   **Parent:** Nexirift Staff
    -   **Attributes:**
        `notes: "This is for developer related services, such as: Sentry, etc."`

## Policies

To see the policies that we use, see the [Policies](./policies) directory.

## Applications

To see the applications that we use, see the [Applications](./applications)
directory.

## Property Mappings

To see the property mappings that we use, see the
[Property Mappings](./property-mappings) directory.

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
