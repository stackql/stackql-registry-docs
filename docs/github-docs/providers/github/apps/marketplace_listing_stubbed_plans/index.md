---
title: marketplace_listing_stubbed_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_listing_stubbed_plans
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
<tr><td><b>Name</b></td><td><code>marketplace_listing_stubbed_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.marketplace_listing_stubbed_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `description` | `string` |
| `number` | `integer` |
| `url` | `string` |
| `state` | `string` |
| `has_free_trial` | `boolean` |
| `unit_name` | `string` |
| `yearly_price_in_cents` | `integer` |
| `bullets` | `array` |
| `accounts_url` | `string` |
| `price_model` | `string` |
| `monthly_price_in_cents` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_plans_stubbed` | `SELECT` |  |
