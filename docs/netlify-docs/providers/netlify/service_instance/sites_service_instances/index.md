---
title: sites_service_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - netlify
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `env` | `object` |
| `auth_url` | `string` |
| `external_attributes` | `object` |
| `service_path` | `string` |
| `config` | `object` |
| `service_slug` | `string` |
| `snippets` | `array` |
| `url` | `string` |
| `service_name` | `string` |
| `updated_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listServiceInstancesForSite` | `SELECT` | `site_id` |
