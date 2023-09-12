---
title: orgs_installation
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs_installation
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
<tr><td><b>Name</b></td><td><code>orgs_installation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.orgs_installation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the installation. |
| `created_at` | `string` |  |
| `single_file_paths` | `array` |  |
| `suspended_by` | `object` | A GitHub user. |
| `app_slug` | `string` |  |
| `has_multiple_single_files` | `boolean` |  |
| `suspended_at` | `string` |  |
| `single_file_name` | `string` |  |
| `access_tokens_url` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `contact_email` | `string` |  |
| `target_type` | `string` |  |
| `account` | `object` | A GitHub user. |
| `repositories_url` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `updated_at` | `string` |  |
| `app_id` | `integer` |  |
| `html_url` | `string` |  |
| `permissions` | `object` | The permissions granted to the user access token. |
| `events` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_org_installation` | `SELECT` | `org` |
