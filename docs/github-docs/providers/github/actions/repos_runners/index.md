---
title: repos_runners
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_runners
  - actions
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
<tr><td><b>Name</b></td><td><code>repos_runners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.repos_runners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The id of the runner. |
| `name` | `string` | The name of the runner. |
| `labels` | `array` |  |
| `os` | `string` | The Operating System of the runner. |
| `runner_group_id` | `integer` | The id of the runner group. |
| `status` | `string` | The status of the runner. |
| `busy` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_self_hosted_runner_for_repo` | `SELECT` | `owner, repo, runner_id` | Gets a specific self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| `list_self_hosted_runners_for_repo` | `SELECT` | `owner, repo` | Lists all self-hosted runners configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| `delete_self_hosted_runner_from_repo` | `DELETE` | `owner, repo, runner_id` | Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
| `generate_runner_jitconfig_for_repo` | `EXEC` | `owner, repo, data__labels, data__name, data__runner_group_id` | Generates a configuration that can be passed to the runner application at startup.<br /><br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br />If the repository is private, you must use an access token with the `repo` scope.<br />GitHub Apps must have the `administration` permission for repositories and the `organization_self_hosted_runners` permission for organizations.<br />Authenticated users must have admin access to repositories or organizations, or the `manage_runners:enterprise` scope for enterprises, to use these endpoints. |
