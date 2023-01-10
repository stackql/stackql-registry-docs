---
title: marketplace_listing_plans_stubbed
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_listing_plans_stubbed
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
| `state` | `string` |
| `unit_name` | `string` |
| `url` | `string` |
| `price_model` | `string` |
| `accounts_url` | `string` |
| `number` | `integer` |
| `yearly_price_in_cents` | `integer` |
| `monthly_price_in_cents` | `integer` |
| `bullets` | `array` |
| `has_free_trial` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_plans_stubbed` | `SELECT` |  |
