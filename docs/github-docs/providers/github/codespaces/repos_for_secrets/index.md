---
title: repos_for_secrets
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
<tr><td><b>Name</b></td><td><code>repos_for_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.repos_for_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `repositories` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repositories_for_secret_for_authenticated_user` | `SELECT` | `secret_name` | List the repositories that have been granted the ability to use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `add_repository_for_secret_for_authenticated_user` | `INSERT` | `repository_id, secret_name` | Adds a repository to the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `remove_repository_for_secret_for_authenticated_user` | `DELETE` | `repository_id, secret_name` | Removes a repository from the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
| `set_repositories_for_secret_for_authenticated_user` | `EXEC` | `secret_name, data__selected_repository_ids` | Select the repositories that will use a user's codespace secret.<br />You must authenticate using an access token with the `user` or `read:user` scope to use this endpoint. User must have Codespaces access to use this endpoint. |
