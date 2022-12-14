---
title: dedicated_hsm
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hsm
  - hardware_security_modules
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
<tr><td><b>Name</b></td><td><code>dedicated_hsm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hardware_security_modules.dedicated_hsm</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Azure Resource Manager resource ID for the dedicated HSM. |
| `name` | `string` | The name of the dedicated HSM. |
| `location` | `string` | The supported Azure location where the dedicated HSM should be created. |
| `tags` | `object` | Resource tags |
| `systemData` | `object` | Metadata pertaining to creation and last modification of dedicated hsm resource. |
| `sku` | `object` | SKU of the dedicated HSM |
| `properties` | `object` | Properties of the dedicated hsm |
| `zones` | `array` | The Dedicated Hsm zones. |
| `type` | `string` | The resource type of the dedicated HSM. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DedicatedHsm_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets the specified Azure dedicated HSM. |
| `DedicatedHsm_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group. |
| `DedicatedHsm_ListBySubscription` | `SELECT` | `subscriptionId` | The List operation gets information about the dedicated HSMs associated with the subscription. |
| `DedicatedHsm_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId, data__location, data__properties, data__sku` | Create or Update a dedicated HSM in the specified subscription. |
| `DedicatedHsm_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Deletes the specified Azure Dedicated HSM. |
| `DedicatedHsm_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `name, resourceGroupName, subscriptionId` | Gets a list of egress endpoints (network endpoints of all outbound dependencies) in the specified dedicated hsm resource. The operation returns properties of each egress endpoint. |
| `DedicatedHsm_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update a dedicated HSM in the specified subscription. |
