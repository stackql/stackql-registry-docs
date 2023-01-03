---
title: sites_dns
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
<tr><td><b>Name</b></td><td><code>sites_dns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.dns_zone.sites_dns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `supported_record_types` | `array` |
| `domain` | `string` |
| `site_id` | `string` |
| `user_id` | `string` |
| `dedicated` | `boolean` |
| `ipv6_enabled` | `boolean` |
| `records` | `array` |
| `account_slug` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `account_name` | `string` |
| `dns_servers` | `array` |
| `errors` | `array` |
| `account_id` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getDNSForSite` | `SELECT` | `site_id` |
| `configureDNSForSite` | `EXEC` | `site_id` |
