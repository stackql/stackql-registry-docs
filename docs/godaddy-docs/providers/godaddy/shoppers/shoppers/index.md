---
title: shoppers
hide_title: false
hide_table_of_contents: false
keywords:
  - shoppers
  - shoppers
  - godaddy    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GoDaddy resources using SQL
custom_edit_url: null
image: /img/providers/godaddy/stackql-godaddy-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shoppers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.shoppers.shoppers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `email` | `string` |
| `externalId` | `integer` |
| `marketId` | `string` |
| `nameFirst` | `string` |
| `nameLast` | `string` |
| `shopperId` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `shopper_id` | Get details for the specified Shopper |
| `update` | `EXEC` | `shopper_id` | Update details for the specified Shopper |
