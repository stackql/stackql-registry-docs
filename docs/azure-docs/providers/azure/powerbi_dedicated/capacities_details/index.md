---
title: capacities_details
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities_details
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
<tr><td><b>Name</b></td><td><code>capacities_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.powerbi_dedicated.capacities_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | An identifier that represents the PowerBI Dedicated resource. |
| `name` | `string` | The name of the PowerBI Dedicated resource. |
| `location` | `string` | Location of the PowerBI Dedicated resource. |
| `properties` | `object` | Properties of Dedicated Capacity resource. |
| `sku` | `object` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Key-value pairs of additional resource provisioning properties. |
| `type` | `string` | The type of the PowerBI Dedicated resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `dedicatedCapacityName, resourceGroupName, subscriptionId` |
