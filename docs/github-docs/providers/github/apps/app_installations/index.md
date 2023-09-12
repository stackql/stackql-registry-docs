---
title: app_installations
hide_title: false
hide_table_of_contents: false
keywords:
  - app_installations
  - apps
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
<tr><td><b>Name</b></td><td><code>app_installations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.app_installations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the installation. |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `app_slug` | `string` |  |
| `target_type` | `string` |  |
| `app_id` | `integer` |  |
| `permissions` | `object` | The permissions granted to the user access token. |
| `suspended_at` | `string` |  |
| `repositories_url` | `string` |  |
| `updated_at` | `string` |  |
| `single_file_name` | `string` |  |
| `suspended_by` | `object` | A GitHub user. |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `contact_email` | `string` |  |
| `single_file_paths` | `array` |  |
| `has_multiple_single_files` | `boolean` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `access_tokens_url` | `string` |  |
| `account` | `object` | A GitHub user. |
| `events` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_installation` | `SELECT` | `installation_id` | Enables an authenticated GitHub App to find an installation's information using the installation id.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `list_installations` | `SELECT` |  | You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.<br /><br />The permissions the installation has are included under the `permissions` key. |
| `delete_installation` | `DELETE` | `installation_id` | Uninstalls a GitHub App on a user, organization, or business account. If you prefer to temporarily suspend an app's access to your account's resources, then we recommend the "[Suspend an app installation](https://docs.github.com/rest/apps/apps#suspend-an-app-installation)" endpoint.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `suspend_installation` | `EXEC` | `installation_id` | Suspends a GitHub App on a user, organization, or business account, which blocks the app from accessing the account's resources. When a GitHub App is suspended, the app's access to the GitHub API or webhook events is blocked for that account.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `unsuspend_installation` | `EXEC` | `installation_id` | Removes a GitHub App installation suspension.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
