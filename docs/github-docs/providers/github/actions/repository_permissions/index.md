---
title: repository_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - actions
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repository_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `selected_actions_url` | `string` | The API URL to use to get or set the actions that are allowed to run, when `allowed_actions` is set to `selected`. |
| `allowed_actions` | `string` | The permissions policy that controls the actions that are allowed to run. Can be one of: `all`, `local_only`, or `selected`. |
| `enabled` | `boolean` | Whether GitHub Actions is enabled on the repository. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_github_actions_permissions_repository` | `SELECT` | `owner, repo` | Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is enabled and the actions allowed to run in the repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. GitHub Apps must have the `administration` repository permission to use this API. |
| `set_github_actions_permissions_repository` | `EXEC` | `owner, repo, data__enabled` | Sets the GitHub Actions permissions policy for enabling GitHub Actions and allowed actions in the repository.<br /><br />If the repository belongs to an organization or enterprise that has set restrictive permissions at the organization or enterprise levels, such as `allowed_actions` to `selected` actions, then you cannot override them for the repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API. |
