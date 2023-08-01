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
| `permissions` | `object` | The permissions granted to the user-to-server access token. |
| `access_tokens_url` | `string` |  |
| `created_at` | `string` |  |
| `account` | `` |  |
| `target_type` | `string` |  |
| `suspended_at` | `string` |  |
| `suspended_by` | `object` | Simple User |
| `html_url` | `string` |  |
| `has_multiple_single_files` | `boolean` |  |
| `contact_email` | `string` |  |
| `target_id` | `integer` | The ID of the user or organization this token is being scoped to. |
| `events` | `array` |  |
| `single_file_name` | `string` |  |
| `app_slug` | `string` |  |
| `app_id` | `integer` |  |
| `repositories_url` | `string` |  |
| `repository_selection` | `string` | Describe whether all repositories have been selected or there's a selection involved |
| `single_file_paths` | `array` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_app_installations` | `SELECT` | `org` |
