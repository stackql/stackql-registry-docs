---
title: actions_permissions
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
<tr><td><b>Name</b></td><td><code>actions_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.actions_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enabled_organizations` | `string` | The policy that controls the organizations in the enterprise that are allowed to run GitHub Actions. Can be one of: `all`, `none`, or `selected`. |
| `selected_actions_url` | `string` | The API URL to use to get or set the actions that are allowed to run, when `allowed_actions` is set to `selected`. |
| `selected_organizations_url` | `string` | The API URL to use to get or set the selected organizations that are allowed to run GitHub Actions, when `enabled_organizations` is set to `selected`. |
| `allowed_actions` | `string` | The permissions policy that controls the actions that are allowed to run. Can be one of: `all`, `local_only`, or `selected`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_github_actions_permissions_enterprise` | `SELECT` | `enterprise` | Gets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.<br /><br />You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint. |
| `set_github_actions_permissions_enterprise` | `EXEC` | `enterprise, data__enabled_organizations` | Sets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.<br /><br />You must authenticate using an access token with the `admin:enterprise` scope to use this endpoint. |
