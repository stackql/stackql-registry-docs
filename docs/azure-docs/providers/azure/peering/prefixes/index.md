---
title: prefixes
hide_title: false
hide_table_of_contents: false
keywords:
  - prefixes
  - peering
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
<tr><td><b>Name</b></td><td><code>prefixes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.peering.prefixes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the resource. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `properties` | `object` | The peering service prefix properties class. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Prefixes_Get` | `SELECT` | `peeringServiceName, prefixName, resourceGroupName, subscriptionId` | Gets an existing prefix with the specified name under the given subscription, resource group and peering service. |
| `Prefixes_ListByPeeringService` | `SELECT` | `peeringServiceName, resourceGroupName, subscriptionId` | Lists all prefixes under the given subscription, resource group and peering service. |
| `Prefixes_CreateOrUpdate` | `INSERT` | `peeringServiceName, prefixName, resourceGroupName, subscriptionId` | Creates a new prefix with the specified name under the given subscription, resource group and peering service. |
| `Prefixes_Delete` | `DELETE` | `peeringServiceName, prefixName, resourceGroupName, subscriptionId` | Deletes an existing prefix with the specified name under the given subscription, resource group and peering service. |
