---
title: credential_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credential_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.credential_authorizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `credential_accessed_at` | `string` | Date when the credential was last accessed. May be null if it was never accessed |
| `credential_type` | `string` | Human-readable description of the credential type. |
| `token_last_eight` | `string` | Last eight characters of the credential. Only included in responses with credential_type of personal access token. |
| `authorized_credential_id` | `integer` |  |
| `credential_id` | `integer` | Unique identifier for the credential. |
| `fingerprint` | `string` | Unique string to distinguish the credential. Only included in responses with credential_type of SSH Key. |
| `scopes` | `array` | List of oauth scopes the token has been granted. |
| `authorized_credential_expires_at` | `string` | The expiry for the token. This will only be present when the credential is a token. |
| `login` | `string` | User login that owns the underlying credential. |
| `authorized_credential_title` | `string` | The title given to the ssh key. This will only be present when the credential is an ssh key. |
| `authorized_credential_note` | `string` | The note given to the token. This will only be present when the credential is a token. |
| `credential_authorized_at` | `string` | Date when the credential was authorized for use. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_saml_sso_authorizations` | `SELECT` | `org` | Listing and deleting credential authorizations is available to organizations with GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products).<br /><br />An authenticated organization owner with the `read:org` scope can list all credential authorizations for an organization that uses SAML single sign-on (SSO). The credentials are either personal access tokens or SSH keys that organization members have authorized for the organization. For more information, see [About authentication with SAML single sign-on](https://docs.github.com/en/articles/about-authentication-with-saml-single-sign-on). |
| `remove_saml_sso_authorization` | `DELETE` | `credential_id, org` | Listing and deleting credential authorizations is available to organizations with GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products).<br /><br />An authenticated organization owner with the `admin:org` scope can remove a credential authorization for an organization that uses SAML SSO. Once you remove someone's credential authorization, they will need to create a new personal access token or SSH key and authorize it for the organization they want to access. |
