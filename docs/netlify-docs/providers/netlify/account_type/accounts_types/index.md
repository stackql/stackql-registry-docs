---
title: accounts_types
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_types
  - account_type
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
<tr><td><b>Name</b></td><td><code>accounts_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.account_type.accounts_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `description` | `string` |
| `yearly_seats_addon_dollar_price` | `integer` |
| `capabilities` | `object` |
| `monthly_dollar_price` | `integer` |
| `monthly_seats_addon_dollar_price` | `integer` |
| `yearly_dollar_price` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `listAccountTypesForUser` | `SELECT` |  |
