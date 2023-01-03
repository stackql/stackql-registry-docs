---
title: marketplace_listing_plans_stubbed
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplace_listing_plans_stubbed</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.marketplace_listing_plans_stubbed</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `description` | `string` |
| `accounts_url` | `string` |
| `number` | `integer` |
| `state` | `string` |
| `url` | `string` |
| `yearly_price_in_cents` | `integer` |
| `price_model` | `string` |
| `has_free_trial` | `boolean` |
| `unit_name` | `string` |
| `monthly_price_in_cents` | `integer` |
| `bullets` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_plans_stubbed` | `SELECT` |  |
