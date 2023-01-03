---
title: self_hosted_runner_groups
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
<tr><td><b>Name</b></td><td><code>self_hosted_runner_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runner_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `number` |  |
| `name` | `string` |  |
| `inherited` | `boolean` |  |
| `selected_repositories_url` | `string` | Link to the selected repositories resource for this runner group. Not present unless visibility was set to `selected` |
| `allows_public_repositories` | `boolean` |  |
| `inherited_allows_public_repositories` | `boolean` |  |
| `default` | `boolean` |  |
| `runners_url` | `string` |  |
| `visibility` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_self_hosted_runner_group_for_org` | `SELECT` | `org, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Gets a specific self-hosted runner group for an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `list_self_hosted_runner_groups_for_org` | `SELECT` | `org` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `create_self_hosted_runner_group_for_org` | `INSERT` | `org, data__name` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Creates a new self-hosted runner group for an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `delete_self_hosted_runner_group_from_org` | `DELETE` | `org, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Deletes a self-hosted runner group for an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `update_self_hosted_runner_group_for_org` | `EXEC` | `org, runner_group_id, data__name` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Updates the `name` and `visibility` of a self-hosted runner group in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
