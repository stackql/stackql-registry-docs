---
title: self_hosted_runner_groups
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
<tr><td><b>Name</b></td><td><code>self_hosted_runner_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.self_hosted_runner_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `number` |
| `name` | `string` |
| `runners_url` | `string` |
| `selected_organizations_url` | `string` |
| `visibility` | `string` |
| `allows_public_repositories` | `boolean` |
| `default` | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_self_hosted_runner_group_for_enterprise` | `SELECT` | `enterprise, runner_group_id` | Gets a specific self-hosted runner group for an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `list_self_hosted_runner_groups_for_enterprise` | `SELECT` | `enterprise` | Lists all self-hosted runner groups for an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `create_self_hosted_runner_group_for_enterprise` | `INSERT` | `enterprise, data__name` | Creates a new self-hosted runner group for an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `delete_self_hosted_runner_group_from_enterprise` | `DELETE` | `enterprise, runner_group_id` | Deletes a self-hosted runner group for an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `update_self_hosted_runner_group_for_enterprise` | `EXEC` | `enterprise, runner_group_id` | Updates the `name` and `visibility` of a self-hosted runner group in an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
