---
title: orders
hide_title: false
hide_table_of_contents: false
keywords:
  - orders
  - orders
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
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>godaddy.orders.orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `domains` | `array` | A collection of domain names purchased if the current product is domain |
| `label` | `string` | Human readable description of the current product |
| `period` | `number` |  |
| `periodUnit` | `string` | The unit of time that periodCount is measured in |
| `pfid` | `integer` | Unique identifier of the current product |
| `pricing` | `object` |  |
| `quantity` | `integer` | Number of the current product included in the specified order |
| `taxCollector` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `order_id` |
| `list` | `SELECT` |  |
