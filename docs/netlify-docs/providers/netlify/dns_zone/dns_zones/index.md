---
title: dns_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_zones
  - dns_zone
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
<tr><td><b>Name</b></td><td><code>dns_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.dns_zones</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `account_slug` | `string` |
| `domain` | `string` |
| `ipv6_enabled` | `boolean` |
| `supported_record_types` | `array` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `dns_servers` | `array` |
| `errors` | `array` |
| `records` | `array` |
| `site_id` | `string` |
| `user_id` | `string` |
| `dedicated` | `boolean` |
| `account_id` | `string` |
| `account_name` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDnsZone` | `SELECT` | `zone_id` |
| `getDnsZones` | `SELECT` |  |
| `createDnsZone` | `INSERT` |  |
| `deleteDnsZone` | `DELETE` | `zone_id` |
