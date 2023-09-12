---
title: users_installation
hide_title: false
hide_table_of_contents: false
keywords:
  - users_installation
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
<tr><td><b>Name</b></td><td><code>users_installation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.users_installation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the installation. |
| `app_slug` | `string` |  |
| `single_file_name` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `account` | `object` | A GitHub user. |
| `html_url` | `string` |  |
| `suspended_at` | `string` |  |
| `target_type` | `string` |  |
| `events` | `array` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `access_tokens_url` | `string` |  |
| `repositories_url` | `string` |  |
| `suspended_by` | `object` | A GitHub user. |
| `app_id` | `integer` |  |
| `contact_email` | `string` |  |
| `single_file_paths` | `array` |  |
| `permissions` | `object` | The permissions granted to the user access token. |
| `created_at` | `string` |  |
| `has_multiple_single_files` | `boolean` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_user_installation` | `SELECT` | `username` |
