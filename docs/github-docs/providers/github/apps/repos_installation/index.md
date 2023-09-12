---
title: repos_installation
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_installation
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
<tr><td><b>Name</b></td><td><code>repos_installation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.repos_installation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the installation. |
| `app_id` | `integer` |  |
| `account` | `object` | A GitHub user. |
| `events` | `array` |  |
| `suspended_by` | `object` | A GitHub user. |
| `has_multiple_single_files` | `boolean` |  |
| `target_type` | `string` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `access_tokens_url` | `string` |  |
| `contact_email` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `updated_at` | `string` |  |
| `app_slug` | `string` |  |
| `single_file_paths` | `array` |  |
| `permissions` | `object` | The permissions granted to the user access token. |
| `suspended_at` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `repositories_url` | `string` |  |
| `single_file_name` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_repo_installation` | `SELECT` | `owner, repo` |
