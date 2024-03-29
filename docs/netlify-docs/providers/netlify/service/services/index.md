---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - service
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.service.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `created_at` | `string` |
| `long_description` | `string` |
| `slug` | `string` |
| `environments` | `array` |
| `tags` | `array` |
| `service_path` | `string` |
| `events` | `array` |
| `icon` | `string` |
| `updated_at` | `string` |
| `manifest_url` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getServices` | `SELECT` |  |
| `showService` | `EXEC` | `addonName` |
