---
title: org_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - org_secrets
  - actions
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
<tr><td><b>Name</b></td><td><code>org_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.org_secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the secret. |
| `selected_repositories_url` | `string` |  |
| `updated_at` | `string` |  |
| `visibility` | `string` | Visibility of a secret |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_org_secret` | `SELECT` | `org, secret_name` | Gets a single organization secret without revealing its encrypted value.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `secrets` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `list_org_secrets` | `SELECT` | `org` | Lists all secrets available in an organization without revealing their<br />encrypted values.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `secrets` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `delete_org_secret` | `DELETE` | `org, secret_name` | Deletes a secret in an organization using the secret name.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `secrets` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `create_or_update_org_secret` | `EXEC` | `org, secret_name, data__visibility` | Creates or updates an organization secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `secrets` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
