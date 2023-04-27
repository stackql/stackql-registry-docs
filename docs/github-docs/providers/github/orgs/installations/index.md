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
| `html_url` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `target_type` | `string` |  |
| `events` | `array` |  |
| `account` | `` |  |
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
| `single_file_paths` | `array` |  |
| `has_multiple_single_files` | `boolean` |  |
| `suspended_by` | `object` | Simple User |
| `suspended_at` | `string` |  |
| `created_at` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `repositories_url` | `string` |  |
| `app_id` | `integer` |  |
| `app_slug` | `string` |  |
| `access_tokens_url` | `string` |  |
| `single_file_name` | `string` |  |
| `updated_at` | `string` |  |
| `contact_email` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_app_installations` | `SELECT` | `org` |
