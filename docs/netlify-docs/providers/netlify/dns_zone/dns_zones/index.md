---
title: dns_zones
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
<tr><td><b>Name</b></td><td><code>dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.dns_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `errors` | `array` |
| `account_name` | `string` |
| `account_slug` | `string` |
| `supported_record_types` | `array` |
| `records` | `array` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `ipv6_enabled` | `boolean` |
| `domain` | `string` |
| `dedicated` | `boolean` |
| `account_id` | `string` |
| `dns_servers` | `array` |
| `user_id` | `string` |
| `site_id` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDnsZone` | `SELECT` | `zone_id` |
| `getDnsZones` | `SELECT` |  |
| `createDnsZone` | `INSERT` |  |
| `deleteDnsZone` | `DELETE` | `zone_id` |
