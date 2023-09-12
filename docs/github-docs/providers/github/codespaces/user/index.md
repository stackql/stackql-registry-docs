---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.codespaces.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` | Automatically generated name of this codespace. |
| `retention_expires_at` | `string` | When a codespace will be auto-deleted based on the "retention_period_minutes" and "last_used_at" |
| `web_url` | `string` | URL to access this codespace on the web. |
| `machine` | `object` | A description of the machine powering a codespace. |
| `url` | `string` | API URL for this codespace. |
| `owner` | `object` | A GitHub user. |
| `environment_id` | `string` | UUID identifying this codespace's environment. |
| `retention_period_minutes` | `integer` | Duration in minutes after codespace has gone idle in which it will be deleted. Must be integer minutes between 0 and 43200 (30 days). |
| `recent_folders` | `array` |  |
| `start_url` | `string` | API URL to start this codespace. |
| `display_name` | `string` | Display name for this codespace. |
| `publish_url` | `string` | API URL to publish this codespace to a new repository. |
| `pending_operation_disabled_reason` | `string` | Text to show user when codespace is disabled by a pending operation |
| `state` | `string` | State of this codespace. |
| `machines_url` | `string` | API URL to access available alternate machine types for this codespace. |
| `devcontainer_path` | `string` | Path to devcontainer.json from repo root used to create Codespace. |
| `created_at` | `string` |  |
| `pulls_url` | `string` | API URL for the Pull Request associated with this codespace, if any. |
| `pending_operation` | `boolean` | Whether or not a codespace has a pending async operation. This would mean that the codespace is temporarily unavailable. The only thing that you can do with a codespace in this state is delete it. |
| `runtime_constraints` | `object` |  |
| `idle_timeout_minutes` | `integer` | The number of minutes of inactivity after which this codespace will be automatically stopped. |
| `prebuild` | `boolean` | Whether the codespace was created from a prebuild. |
| `idle_timeout_notice` | `string` | Text to show user when codespace idle timeout minutes has been overriden by an organization policy |
| `location` | `string` | The initally assigned location of a new codespace. |
| `updated_at` | `string` |  |
| `stop_url` | `string` | API URL to stop this codespace. |
| `last_known_stop_notice` | `string` | The text to display to a user when a codespace has been stopped for a potentially actionable reason. |
| `billable_owner` | `object` | A GitHub user. |
| `git_status` | `object` | Details about the codespace's git repository. |
| `repository` | `object` | Minimal Repository |
| `last_used_at` | `string` | Last known time this codespace was started. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_for_authenticated_user` | `SELECT` | `codespace_name` | Gets information about a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces` repository permission to use this endpoint. |
| `list_for_authenticated_user` | `SELECT` |  | Lists the authenticated user's codespaces.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces` repository permission to use this endpoint. |
| `create_for_authenticated_user` | `INSERT` |  | Creates a new codespace, owned by the authenticated user.<br /><br />This endpoint requires either a `repository_id` OR a `pull_request` but not both.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| `delete_for_authenticated_user` | `DELETE` | `codespace_name` | Deletes a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| `codespace_machines_for_authenticated_user` | `EXEC` | `codespace_name` | List the machine types a codespace can transition to use.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have read access to the `codespaces_metadata` repository permission to use this endpoint. |
| `publish_for_authenticated_user` | `EXEC` | `codespace_name` | Publishes an unpublished codespace, creating a new repository and assigning it to the codespace.<br /><br />The codespace's token is granted write permissions to the repository, allowing the user to push their changes.<br /><br />This will fail for a codespace that is already published, meaning it has an associated repository.<br /><br />You must authenticate using a personal access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
| `start_for_authenticated_user` | `EXEC` | `codespace_name` | Starts a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_lifecycle_admin` repository permission to use this endpoint. |
| `stop_for_authenticated_user` | `EXEC` | `codespace_name` | Stops a user's codespace.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces_lifecycle_admin` repository permission to use this endpoint. |
| `update_for_authenticated_user` | `EXEC` | `codespace_name` | Updates a codespace owned by the authenticated user. Currently only the codespace's machine type and recent folders can be modified using this endpoint.<br /><br />If you specify a new machine type it will be applied the next time your codespace is started.<br /><br />You must authenticate using an access token with the `codespace` scope to use this endpoint.<br /><br />GitHub Apps must have write access to the `codespaces` repository permission to use this endpoint. |
