---
title: environments_deployment_branch_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_deployment_branch_policies
  - repos
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
<tr><td><b>Name</b></td><td><code>environments_deployment_branch_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.environments_deployment_branch_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The unique identifier of the branch policy. |
| `name` | `string` | The name pattern that branches must match in order to deploy to the environment. |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_deployment_branch_policy` | `SELECT` | `branch_policy_id, environment_name, owner, repo` | Gets a deployment branch policy for an environment.<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `list_deployment_branch_policies` | `SELECT` | `environment_name, owner, repo` | Lists the deployment branch policies for an environment.<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `create_deployment_branch_policy` | `INSERT` | `environment_name, owner, repo, data__name` | Creates a deployment branch policy for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration:write` permission for the repository to use this endpoint. |
| `delete_deployment_branch_policy` | `DELETE` | `branch_policy_id, environment_name, owner, repo` | Deletes a deployment branch policy for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration:write` permission for the repository to use this endpoint. |
| `update_deployment_branch_policy` | `EXEC` | `branch_policy_id, environment_name, owner, repo, data__name` | Updates a deployment branch policy for an environment.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration:write` permission for the repository to use this endpoint. |
