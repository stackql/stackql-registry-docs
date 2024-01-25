---
title: capacities_skus_for_capacity
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_skus_for_capacity
  - powerbi_dedicated
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
<tr><td><b>Name</b></td><td><code>capacities_skus_for_capacity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_dedicated.capacities_skus_for_capacity</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceType` | `string` | The resource type |
| `sku` | `object` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `dedicatedCapacityName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `dedicatedCapacityName, resourceGroupName, subscriptionId` |
