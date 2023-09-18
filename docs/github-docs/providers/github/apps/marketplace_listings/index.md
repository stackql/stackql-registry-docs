---
title: marketplace_listings
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_listings
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
<tr><td><b>Name</b></td><td><code>marketplace_listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.apps.marketplace_listings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `description` | `string` |
| `number` | `integer` |
| `state` | `string` |
| `bullets` | `array` |
| `yearly_price_in_cents` | `integer` |
| `url` | `string` |
| `unit_name` | `string` |
| `price_model` | `string` |
| `accounts_url` | `string` |
| `monthly_price_in_cents` | `integer` |
| `has_free_trial` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_plans` | `SELECT` |  |
