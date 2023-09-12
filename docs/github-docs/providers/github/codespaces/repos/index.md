---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `codespaces` | `array` |
| `total_count` | `integer` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_in_repository_for_authenticated_user` | `SELECT` | `owner, repo` | Lists the codespaces associated to a specified repository and the authenticated user.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces` repository permission to use this endpoint. |
| `create_with_repo_for_authenticated_user` | `INSERT` | `owner, repo` | Creates a codespace owned by the authenticated user in the specified repository.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| `pre_flight_with_repo_for_authenticated_user` | `EXEC` | `owner, repo` | Gets the default attributes for codespaces created by the user with the repository.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| `repo_machines_for_authenticated_user` | `EXEC` | `owner, repo` | List the machine types available for a given repository based on its configuration.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_metadata` repository permission to use this endpoint. |
