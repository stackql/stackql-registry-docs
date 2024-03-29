---
title: gpg_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - gpg_keys
  - users
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gpg_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.gpg_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `public_key` | `string` |
| `can_certify` | `boolean` |
| `subkeys` | `array` |
| `revoked` | `boolean` |
| `raw_key` | `string` |
| `key_id` | `string` |
| `primary_key_id` | `integer` |
| `can_encrypt_comms` | `boolean` |
| `expires_at` | `string` |
| `can_sign` | `boolean` |
| `created_at` | `string` |
| `emails` | `array` |
| `can_encrypt_storage` | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_gpg_key_for_authenticated_user` | `SELECT` | `gpg_key_id` | View extended details for a single GPG key. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| `list_gpg_keys_for_authenticated_user` | `SELECT` |  | Lists the current user's GPG keys. Requires that you are authenticated via Basic Auth or via OAuth with at least `read:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| `list_gpg_keys_for_user` | `SELECT` | `username` | Lists the GPG keys for a user. This information is accessible by anyone. |
| `create_gpg_key_for_authenticated_user` | `INSERT` | `data__armored_public_key` | Adds a GPG key to the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth, or OAuth with at least `write:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
| `delete_gpg_key_for_authenticated_user` | `DELETE` | `gpg_key_id` | Removes a GPG key from the authenticated user's GitHub account. Requires that you are authenticated via Basic Auth or via OAuth with at least `admin:gpg_key` [scope](https://docs.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/). |
