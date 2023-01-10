---
title: sites_service_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_service_instances
  - service_instance
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
<tr><td><b>Name</b></td><td><code>sites_service_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.service_instance.sites_service_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `external_attributes` | `object` |
| `service_name` | `string` |
| `service_slug` | `string` |
| `snippets` | `array` |
| `auth_url` | `string` |
| `service_path` | `string` |
| `url` | `string` |
| `config` | `object` |
| `env` | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listServiceInstancesForSite` | `SELECT` | `site_id` |
