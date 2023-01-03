---
title: org_access_to_self_hosted_runner_group
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
<tr><td><b>Name</b></td><td><code>org_access_to_self_hosted_runner_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.org_access_to_self_hosted_runner_group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `total_count` | `number` |
| `organizations` | `array` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_org_access_to_self_hosted_runner_group_in_enterprise` | `SELECT` | `enterprise, runner_group_id` | Lists the organizations with access to a self-hosted runner group.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `add_org_access_to_self_hosted_runner_group_in_enterprise` | `INSERT` | `enterprise, org_id, runner_group_id` | Adds an organization to the list of selected organizations that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise)."<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `remove_org_access_to_self_hosted_runner_group_in_enterprise` | `DELETE` | `enterprise, org_id, runner_group_id` | Removes an organization from the list of selected organizations that can access a self-hosted runner group. The runner group must have `visibility` set to `selected`. For more information, see "[Create a self-hosted runner group for an enterprise](#create-a-self-hosted-runner-group-for-an-enterprise)."<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `set_org_access_to_self_hosted_runner_group_in_enterprise` | `EXEC` | `enterprise, runner_group_id, data__selected_organization_ids` | Replaces the list of organizations that have access to a self-hosted runner configured in an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
