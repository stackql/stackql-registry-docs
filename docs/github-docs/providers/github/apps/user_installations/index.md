---
title: user_installations
hide_title: false
hide_table_of_contents: false
keywords:
  - user_installations
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
<tr><td><b>Name</b></td><td><code>user_installations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.user_installations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the installation. |
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
| `has_multiple_single_files` | `boolean` |  |
| `html_url` | `string` |  |
| `app_slug` | `string` |  |
| `contact_email` | `string` |  |
| `events` | `array` |  |
| `updated_at` | `string` |  |
| `target_type` | `string` |  |
| `single_file_name` | `string` |  |
| `repositories_url` | `string` |  |
| `suspended_by` | `object` | Simple User |
| `account` | `` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `single_file_paths` | `array` |  |
| `app_id` | `integer` |  |
| `created_at` | `string` |  |
| `access_tokens_url` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `suspended_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_user_installation` | `SELECT` | `username` | Enables an authenticated GitHub App to find the user’s installation information.<br /><br />You must use a [JWT](https://docs.github.com/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint. |
| `list_installations_for_authenticated_user` | `SELECT` |  | Lists installations of your GitHub App that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.<br /><br />You must use a [user-to-server OAuth access token](https://docs.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/#identifying-users-on-your-site), created for a user who has authorized your GitHub App, to access this endpoint.<br /><br />The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.<br /><br />You can find the permissions for the installation under the `permissions` key. |
