---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - network
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource identifier. |
| `name` | `object` | The usage names. |
| `unit` | `string` | An enum describing the unit of measurement. |
| `currentValue` | `integer` | The current value of the usage. |
| `limit` | `integer` | The limit of usage. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_List` | `SELECT` | `location, subscriptionId` |
