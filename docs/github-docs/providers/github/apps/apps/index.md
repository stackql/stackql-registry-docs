---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - apps
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
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.apps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the GitHub app |
| `name` | `string` | The name of the GitHub app |
| `description` | `string` |  |
| `node_id` | `string` |  |
| `html_url` | `string` |  |
| `permissions` | `object` | The set of permissions for the GitHub app |
| `external_url` | `string` |  |
| `webhook_secret` | `string` |  |
| `created_at` | `string` |  |
| `pem` | `string` |  |
| `installations_count` | `integer` | The number of installations associated with the GitHub app |
| `client_secret` | `string` |  |
| `client_id` | `string` |  |
| `owner` | `object` | A GitHub user. |
| `updated_at` | `string` |  |
| `events` | `array` | The list of events for the GitHub app |
| `slug` | `string` | The slug name of the GitHub app |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_by_slug` | `SELECT` | `app_slug` |
