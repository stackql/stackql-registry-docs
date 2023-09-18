---
title: organization_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_secrets
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
<tr><td><b>Name</b></td><td><code>organization_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.organization_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the secret |
| `selected_repositories_url` | `string` | The API URL at which the list of repositories this secret is visible to can be retrieved |
| `updated_at` | `string` | The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
| `visibility` | `string` | The type of repositories in the organization that the secret is visible to |
| `created_at` | `string` | The date and time at which the secret was created, in ISO 8601 format':' YYYY-MM-DDTHH:MM:SSZ. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_org_secret` | `SELECT` | `org, secret_name` | Gets an organization secret without revealing its encrypted value.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `list_org_secrets` | `SELECT` | `org` | Lists all Codespaces secrets available at the organization-level without revealing their encrypted values.<br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `delete_org_secret` | `DELETE` | `org, secret_name` | Deletes an organization secret using the secret name. You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `create_or_update_org_secret` | `EXEC` | `org, secret_name, data__visibility` | Creates or updates an organization secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access<br />token with the `admin:org` scope to use this endpoint. |
