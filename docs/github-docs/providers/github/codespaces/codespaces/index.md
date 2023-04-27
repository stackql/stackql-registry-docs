---
title: codespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - codespaces
  - codespaces
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
<tr><td><b>Name</b></td><td><code>codespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.codespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | Automatically generated name of this codespace. |
| `repository` | `object` | Minimal Repository |
| `prebuild` | `boolean` | Whether the codespace was created from a prebuild. |
| `updated_at` | `string` |  |
| `billable_owner` | `object` | Simple User |
| `location` | `string` | The Azure region where this codespace is located. |
| `created_at` | `string` |  |
| `display_name` | `string` | Display name for this codespace. |
| `state` | `string` | State of this codespace. |
| `machine` | `object` | A description of the machine powering a codespace. |
| `last_used_at` | `string` | Last known time this codespace was started. |
| `owner` | `object` | Simple User |
| `url` | `string` | API URL for this codespace. |
| `pulls_url` | `string` | API URL for the Pull Request associated with this codespace, if any. |
| `start_url` | `string` | API URL to start this codespace. |
| `web_url` | `string` | URL to access this codespace on the web. |
| `environment_id` | `string` | UUID identifying this codespace's environment. |
| `git_status` | `object` | Details about the codespace's git repository. |
| `idle_timeout_minutes` | `integer` | The number of minutes of inactivity after which this codespace will be automatically stopped. |
| `machines_url` | `string` | API URL to access available alternate machine types for this codespace. |
| `recent_folders` | `array` |  |
| `stop_url` | `string` | API URL to stop this codespace. |
| `runtime_constraints` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_for_authenticated_user` | `SELECT` | `codespace_name` | Gets information about a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `list_for_authenticated_user` | `SELECT` |  | Lists the authenticated user's codespaces.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `list_in_repository_for_authenticated_user` | `SELECT` | `owner, repo` | Lists the codespaces associated to a specified repository and the authenticated user.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `create_for_authenticated_user` | `INSERT` |  | Creates a new codespace, owned by the authenticated user.<br /><br />This endpoint requires either a `repository_id` OR a `pull_request` but not both.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `create_with_pr_for_authenticated_user` | `INSERT` | `owner, pull_number, repo, data__location` | Creates a codespace owned by the authenticated user for the specified pull request.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `create_with_repo_for_authenticated_user` | `INSERT` | `owner, repo, data__location` | Creates a codespace owned by the authenticated user in the specified repository.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `delete_for_authenticated_user` | `DELETE` | `codespace_name` | Deletes a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `export_for_authenticated_user` | `EXEC` | `codespace_name` | Triggers an export of the specified codespace and returns a URL and ID where the status of the export can be monitored.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint. |
| `get_export_details_for_authenticated_user` | `EXEC` | `codespace_name, export_id` | Gets information about an export of a codespace.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint. |
| `start_for_authenticated_user` | `EXEC` | `codespace_name` | Starts a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `stop_for_authenticated_user` | `EXEC` | `codespace_name` | Stops a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
| `update_for_authenticated_user` | `EXEC` | `codespace_name` | Updates a codespace owned by the authenticated user. Currently only the codespace's machine type and recent folders can be modified using this endpoint.<br /><br />If you specify a new machine type it will be applied the next time your codespace is started.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint. |
