---
title: user_social_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - user_social_accounts
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
<tr><td><b>Name</b></td><td><code>user_social_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.user_social_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `url` | `string` |
| `provider` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_social_accounts_for_authenticated_user` | `SELECT` |  | Lists all of your social accounts. |
| `add_social_account_for_authenticated_user` | `INSERT` | `data__account_urls` | Add one or more social accounts to the authenticated user's profile. This endpoint is accessible with the `user` scope. |
| `delete_social_account_for_authenticated_user` | `DELETE` | `data__account_urls` | Deletes one or more social accounts from the authenticated user's profile. This endpoint is accessible with the `user` scope. |
