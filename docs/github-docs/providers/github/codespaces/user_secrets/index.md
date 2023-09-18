---
title: user_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - user_secrets
  - codespaces
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
<tr><td><b>Name</b></td><td><code>user_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.user_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `total_count` | `integer` |
| `repositories` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repositories_for_secret_for_authenticated_user` | `SELECT` | `secret_name` | List the repositories that have been granted the ability to use a user's codespace secret.<br /><br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must have Codespaces access to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces_user_secrets` user permission and write access to the `codespaces_secrets` repository permission on all referenced repositories to use this endpoint. |
| `remove_repository_for_secret_for_authenticated_user` | `DELETE` | `repository_id, secret_name` | Removes a repository from the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must have Codespaces access to use this endpoint.<br />GitHub Apps must have write access to the `codespaces_user_secrets` user permission to use this endpoint. |
| `add_repository_for_secret_for_authenticated_user` | `EXEC` | `repository_id, secret_name` | Adds a repository to the selected repositories for a user's codespace secret.<br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must have Codespaces access to use this endpoint.<br />GitHub Apps must have write access to the `codespaces_user_secrets` user permission and write access to the `codespaces_secrets` repository permission on the referenced repository to use this endpoint. |
| `set_repositories_for_secret_for_authenticated_user` | `EXEC` | `secret_name, data__selected_repository_ids` | Select the repositories that will use a user's codespace secret.<br /><br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must have Codespaces access to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_user_secrets` user permission and write access to the `codespaces_secrets` repository permission on all referenced repositories to use this endpoint. |
