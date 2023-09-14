---
title: public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - public_keys
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
<tr><td><b>Name</b></td><td><code>public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.public_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `title` | `string` |  |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `key` | `string` | The Base64 encoded public key. |
| `key_id` | `string` | The identifier for the key. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_environment_public_key` | `SELECT` | `environment_name, repository_id` | Get the public key for an environment, which you need to encrypt environment<br />secrets. You need to encrypt a secret before you can create or update secrets.<br /><br />Anyone with read access to the repository can use this endpoint.<br />If the repository is private you must use an access token with the `repo` scope.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `get_org_public_key` | `SELECT` | `org` | Gets your public key, which you need to encrypt secrets. You need to<br />encrypt a secret before you can create or update secrets.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `secrets` organization permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
| `get_repo_public_key` | `SELECT` | `owner, repo` | Gets your public key, which you need to encrypt secrets. You need to<br />encrypt a secret before you can create or update secrets.<br /><br />Anyone with read access to the repository can use this endpoint.<br />If the repository is private you must use an access token with the `repo` scope.<br />GitHub Apps must have the `secrets` repository permission to use this endpoint.<br />Authenticated users must have collaborator access to a repository to create, update, or read secrets. |
