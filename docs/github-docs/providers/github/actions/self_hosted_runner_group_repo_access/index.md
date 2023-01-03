---
title: self_hosted_runner_group_repo_access
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
<tr><td><b>Name</b></td><td><code>self_hosted_runner_group_repo_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runner_group_repo_access</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `total_count` | `number` |
| `repositories` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repo_access_to_self_hosted_runner_group_in_org` | `SELECT` | `org, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud and GitHub Enterprise Server. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Lists the repositories with access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `add_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Adds a repository to the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org`<br />scope to use this endpoint. |
| `remove_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, repository_id, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Removes a repository from the list of selected repositories that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an organization](#create-a-self-hosted-runner-group-for-an-organization)."<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `set_repo_access_to_self_hosted_runner_group_in_org` | `EXEC` | `org, runner_group_id, data__selected_repository_ids` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Replaces the list of repositories that have access to a self-hosted runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
