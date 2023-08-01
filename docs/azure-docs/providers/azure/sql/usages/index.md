---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - sql
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
<tr><td><b>Id</b></td><td><code>azure.sql.usages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `object` | ARM Usage Name |
| `limit` | `integer` | Usage limit. |
| `requestedLimit` | `integer` | Usage requested limit. |
| `type` | `string` | Resource type. |
| `unit` | `string` | Usage unit. |
| `currentValue` | `integer` | Usage current value. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Usages_ListByInstancePool` | `SELECT` | `instancePoolName, resourceGroupName, subscriptionId` |
