---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the secret |
| `created_at` | `string` | The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `selected_repositories_url` | `string` | The API URL at which the list of repositories this secret is visible to can be retrieved |
| `updated_at` | `string` | The date and time at which the secret was last updated, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `visibility` | `string` | The type of repositories in the organization that the secret is visible to |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_secret_for_authenticated_user` | `SELECT` | `secret_name` | Gets a secret available to a user's codespaces without revealing its encrypted value.<br /><br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must have Codespaces access to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces_user_secrets` user permission to use this endpoint. |
| `list_secrets_for_authenticated_user` | `SELECT` |  | Lists all secrets available for a user's Codespaces without revealing their<br />encrypted values.<br /><br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must have Codespaces access to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces_user_secrets` user permission to use this endpoint. |
| `delete_secret_for_authenticated_user` | `DELETE` | `secret_name` | Deletes a secret from a user's codespaces using the secret name. Deleting the secret will remove access from all codespaces that were allowed to access the secret.<br /><br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must have Codespaces access to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_user_secrets` user permission to use this endpoint. |
| `create_or_update_secret_for_authenticated_user` | `EXEC` | `secret_name, data__key_id` | Creates or updates a secret for a user's codespace with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access token with the `codespace` or `codespace:secrets` scope to use this endpoint. User must also have Codespaces access to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_user_secrets` user permission and `codespaces_secrets` repository permission on all referenced repositories to use this endpoint. |
