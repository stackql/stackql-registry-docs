---
title: sites_dns
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_dns
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
<tr><td><b>Name</b></td><td><code>sites_dns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.sites_dns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `dedicated` | `boolean` |
| `user_id` | `string` |
| `errors` | `array` |
| `updated_at` | `string` |
| `site_id` | `string` |
| `domain` | `string` |
| `dns_servers` | `array` |
| `ipv6_enabled` | `boolean` |
| `records` | `array` |
| `account_slug` | `string` |
| `account_id` | `string` |
| `supported_record_types` | `array` |
| `account_name` | `string` |
| `created_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDNSForSite` | `SELECT` | `site_id` |
| `configureDNSForSite` | `EXEC` | `site_id` |
