---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.secrets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of the secret. |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_environment_secret` | `SELECT` | `environment_name, repository_id, secret_name` | Gets a single environment secret without revealing its encrypted value.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `get_repo_secret` | `SELECT` | `owner, repo, secret_name` | Gets a single repository secret without revealing its encrypted value.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `list_environment_secrets` | `SELECT` | `environment_name, repository_id` | Lists all secrets available in an environment without revealing their<br />encrypted values.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `list_repo_secrets` | `SELECT` | `owner, repo` | Lists all secrets available in a repository without revealing their encrypted<br />values.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `delete_environment_secret` | `DELETE` | `environment_name, repository_id, secret_name` | Deletes a secret in an environment using the secret name.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `delete_repo_secret` | `DELETE` | `owner, repo, secret_name` | Deletes a secret in a repository using the secret name.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `create_or_update_environment_secret` | `EXEC` | `environment_name, repository_id, secret_name, data__encrypted_value, data__key_id` | Creates or updates an environment secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `create_or_update_repo_secret` | `EXEC` | `owner, repo, secret_name` | Creates or updates a repository secret with an encrypted value. Encrypt your secret using<br />[LibSodium](https://libsodium.gitbook.io/doc/bindings_for_other_languages). For more information, see "[Encrypting secrets for the REST API](https://docs.github.com/rest/guides/encrypting-secrets-for-the-rest-api)."<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
