---
title: self_hosted_runners
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
<tr><td><b>Name</b></td><td><code>self_hosted_runners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.actions.self_hosted_runners</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The id of the runner. |
| `name` | `string` | The name of the runner. |
| `labels` | `array` |  |
| `os` | `string` | The Operating System of the runner. |
| `status` | `string` | The status of the runner. |
| `busy` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_self_hosted_runner_for_org` | `SELECT` | `org, runner_id` | Gets a specific self-hosted runner configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `get_self_hosted_runner_for_repo` | `SELECT` | `owner, repo, runner_id` | Gets a specific self-hosted runner configured in a repository.<br /><br />You must authenticate using an access token with the `repo` scope to use this<br />endpoint. |
| `list_self_hosted_runners_for_org` | `SELECT` | `org` | Lists all self-hosted runners configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `list_self_hosted_runners_for_repo` | `SELECT` | `owner, repo` | Lists all self-hosted runners configured in a repository. You must authenticate using an access token with the `repo` scope to use this endpoint. |
| `list_self_hosted_runners_in_group_for_org` | `SELECT` | `org, runner_group_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Lists self-hosted runners that are in a specific organization group.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `delete_self_hosted_runner_from_org` | `DELETE` | `org, runner_id` | Forces the removal of a self-hosted runner from an organization. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `delete_self_hosted_runner_from_repo` | `DELETE` | `owner, repo, runner_id` | Forces the removal of a self-hosted runner from a repository. You can use this endpoint to completely remove the runner when the machine you were using no longer exists.<br /><br />You must authenticate using an access token with the `repo`<br />scope to use this endpoint. |
| `remove_self_hosted_runner_from_group_for_org` | `DELETE` | `org, runner_group_id, runner_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Removes a self-hosted runner from a group configured in an organization. The runner is then returned to the default group.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
| `add_self_hosted_runner_to_group_for_org` | `EXEC` | `org, runner_group_id, runner_id` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br /><br />Adds a self-hosted runner to a runner group configured in an organization.<br /><br />You must authenticate using an access token with the `admin:org`<br />scope to use this endpoint. |
| `create_registration_token_for_org` | `EXEC` | `org` | Returns a token that you can pass to the `config` script. The token expires after one hour.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br /><br />#### Example using registration token<br /><br />Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.<br /><br />```<br />./config.sh --url https://github.com/octo-org --token TOKEN<br />``` |
| `create_registration_token_for_repo` | `EXEC` | `owner, repo` | Returns a token that you can pass to the `config` script. The token expires after one hour. You must authenticate<br />using an access token with the `repo` scope to use this endpoint.<br /><br />#### Example using registration token<br /> <br />Configure your self-hosted runner, replacing `TOKEN` with the registration token provided by this endpoint.<br /><br />```<br />./config.sh --url https://github.com/octo-org/octo-repo-artifacts --token TOKEN<br />``` |
| `create_remove_token_for_org` | `EXEC` | `org` | Returns a token that you can pass to the `config` script to remove a self-hosted runner from an organization. The token expires after one hour.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint.<br /><br />#### Example using remove token<br /><br />To remove your self-hosted runner from an organization, replace `TOKEN` with the remove token provided by this<br />endpoint.<br /><br />```<br />./config.sh remove --token TOKEN<br />``` |
| `create_remove_token_for_repo` | `EXEC` | `owner, repo` | Returns a token that you can pass to remove a self-hosted runner from a repository. The token expires after one hour.<br />You must authenticate using an access token with the `repo` scope to use this endpoint.<br /><br />#### Example using remove token<br /> <br />To remove your self-hosted runner from a repository, replace TOKEN with the remove token provided by this endpoint.<br /><br />```<br />./config.sh remove --token TOKEN<br />``` |
| `set_self_hosted_runners_in_group_for_org` | `EXEC` | `org, runner_group_id, data__runners` | The self-hosted runner groups REST API is available with GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)."<br /><br />Replaces the list of self-hosted runners that are part of an organization runner group.<br /><br />You must authenticate using an access token with the `admin:org` scope to use this endpoint. |
