---
title: self_hosted_runners
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
<tr><td><b>Name</b></td><td><code>self_hosted_runners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.enterprise_admin.self_hosted_runners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `runners` | `array` |
| `total_count` | `number` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_self_hosted_runner_for_enterprise` | `SELECT` | `enterprise, runner_id` | Gets a specific self-hosted runner configured in an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `list_self_hosted_runners_for_enterprise` | `SELECT` | `enterprise` | Lists all self-hosted runners configured for an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `list_self_hosted_runners_in_group_for_enterprise` | `SELECT` | `enterprise, runner_group_id` | Lists the self-hosted runners that are in a specific enterprise group.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `add_self_hosted_runner_to_group_for_enterprise` | `INSERT` | `enterprise, runner_group_id, runner_id` | Adds a self-hosted runner to a runner group configured in an enterprise.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise`<br />scope to use this endpoint. |
| `delete_self_hosted_runner_from_enterprise` | `DELETE` | `enterprise, runner_id` | Forces the removal of a self-hosted runner from an enterprise. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `remove_self_hosted_runner_from_group_for_enterprise` | `DELETE` | `enterprise, runner_group_id, runner_id` | Removes a self-hosted runner from a group configured in an enterprise. The runner is then returned to the default group.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
| `create_registration_token_for_enterprise` | `EXEC` | `enterprise` | Returns a token that you can pass to the `config` script. The token expires after one hour.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.<br /><br />#### Example using registration token<br /><br />Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.<br /><br />```<br />./config.sh --url https://github.com/enterprises/octo-enterprise --token TOKEN<br />``` |
| `create_remove_token_for_enterprise` | `EXEC` | `enterprise` | Returns a token that you can pass to the `config` script to remove a self-hosted runner from an enterprise. The token expires after one hour.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint.<br /><br />#### Example using remove token<br /><br />To remove your self-hosted runner from an enterprise, replace `TOKEN` with the remove token provided by this<br />endpoint.<br /><br />```<br />./config.sh remove --token TOKEN<br />``` |
| `set_self_hosted_runners_in_group_for_enterprise` | `EXEC` | `enterprise, runner_group_id, data__runners` | Replaces the list of self-hosted runners that are part of an enterprise runner group.<br /><br />You must authenticate using an access token with the `manage_runners:enterprise` scope to use this endpoint. |
