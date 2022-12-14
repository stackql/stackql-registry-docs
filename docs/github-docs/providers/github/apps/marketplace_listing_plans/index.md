---
title: marketplace_listing_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_listing_plans
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
<tr><td><b>Name</b></td><td><code>marketplace_listing_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.marketplace_listing_plans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `description` | `string` |
| `unit_name` | `string` |
| `yearly_price_in_cents` | `integer` |
| `accounts_url` | `string` |
| `monthly_price_in_cents` | `integer` |
| `price_model` | `string` |
| `state` | `string` |
| `url` | `string` |
| `has_free_trial` | `boolean` |
| `number` | `integer` |
| `bullets` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_plans` | `SELECT` |  |
