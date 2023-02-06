---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The id of the environment. |
| `name` | `string` | The name of the environment. |
| `url` | `string` |  |
| `created_at` | `string` | The time that the environment was created, in ISO 8601 format. |
| `html_url` | `string` |  |
| `protection_rules` | `array` |  |
| `updated_at` | `string` | The time that the environment was last updated, in ISO 8601 format. |
| `node_id` | `string` |  |
| `deployment_branch_policy` | `object` | The type of deployment branch policy for this environment. To allow all branches to deploy, set to `null`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_all_environments` | `SELECT` | `owner, repo` | Get all environments for a repository.<br /><br />Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `get_environment` | `SELECT` | `environment_name, owner, repo` | Anyone with read access to the repository can use this endpoint. If the repository is private, you must use an access token with the `repo` scope. GitHub Apps must have the `actions:read` permission to use this endpoint. |
| `create_or_update_environment` | `INSERT` | `environment_name, owner, repo` | Create or update an environment with protection rules, such as required reviewers. For more information about environment protection rules, see "[Environments](/actions/reference/environments#environment-protection-rules)."<br /><br />**Note:** Although you can use this operation to specify that only branches that match specified name patterns can deploy to this environment, you must use the UI to set the name patterns. For more information, see "[Environments](/actions/reference/environments#deployment-branches)."<br /><br />**Note:** To create or update secrets for an environment, see "[Secrets](/rest/reference/actions#secrets)."<br /><br />You must authenticate using an access token with the repo scope to use this endpoint. |
| `delete_an_environment` | `DELETE` | `environment_name, owner, repo` | You must authenticate using an access token with the repo scope to use this endpoint. |
