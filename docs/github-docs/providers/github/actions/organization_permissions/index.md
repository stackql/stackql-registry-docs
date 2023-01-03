---
title: organization_permissions
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
<tr><td><b>Name</b></td><td><code>organization_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.organization_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enabled_repositories` | `string` | The policy that controls the repositories in the organization that are allowed to run GitHub Actions. Can be one of: `all`, `none`, or `selected`. |
| `selected_actions_url` | `string` | The API URL to use to get or set the actions that are allowed to run, when `allowed_actions` is set to `selected`. |
| `selected_repositories_url` | `string` | The API URL to use to get or set the selected repositories that are allowed to run GitHub Actions, when `enabled_repositories` is set to `selected`. |
| `allowed_actions` | `string` | The permissions policy that controls the actions that are allowed to run. Can be one of: `all`, `local_only`, or `selected`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_github_actions_permissions_organization` | `SELECT` | `org` | Gets the GitHub Actions permissions policy for repositories and allowed actions in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
| `set_github_actions_permissions_organization` | `EXEC` | `org, data__enabled_repositories` | Sets the GitHub Actions permissions policy for repositories and allowed actions in an organization.<br /><br />If the organization belongs to an enterprise that has set restrictive permissions at the enterprise level, such as `allowed_actions` to `selected` actions, then you cannot override them for the organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API. |
