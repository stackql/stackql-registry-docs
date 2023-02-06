---
title: installations
hide_title: false
hide_table_of_contents: false
keywords:
  - installations
  - orgs
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
<tr><td><b>Name</b></td><td><code>installations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.installations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the installation. |
| `repositories_url` | `string` |  |
| `access_tokens_url` | `string` |  |
| `single_file_name` | `string` |  |
| `single_file_paths` | `array` |  |
| `events` | `array` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `has_multiple_single_files` | `boolean` |  |
| `updated_at` | `string` |  |
| `app_id` | `integer` |  |
| `contact_email` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `account` | `` |  |
| `suspended_at` | `string` |  |
| `target_type` | `string` |  |
| `suspended_by` | `object` | Simple User |
| `app_slug` | `string` |  |
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_app_installations` | `SELECT` | `org` |
