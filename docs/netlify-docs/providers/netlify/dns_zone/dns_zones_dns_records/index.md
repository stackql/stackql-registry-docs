---
title: dns_zones_dns_records
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_zones_dns_records
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
<tr><td><b>Name</b></td><td><code>dns_zones_dns_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.dns_zones_dns_records</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `flag` | `integer` |
| `managed` | `boolean` |
| `tag` | `string` |
| `value` | `string` |
| `dns_zone_id` | `string` |
| `priority` | `integer` |
| `type` | `string` |
| `hostname` | `string` |
| `site_id` | `string` |
| `ttl` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDnsRecords` | `SELECT` | `zone_id` |
| `getIndividualDnsRecord` | `SELECT` | `dns_record_id, zone_id` |
| `createDnsRecord` | `INSERT` | `zone_id` |
| `deleteDnsRecord` | `DELETE` | `dns_record_id, zone_id` |
