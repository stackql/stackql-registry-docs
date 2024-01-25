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
| `properties` | `object` | Properties of the dedicated hsm |
| `sku` | `object` | SKU of the dedicated HSM |
| `systemData` | `object` | Metadata pertaining to creation and last modification of dedicated hsm resource. |
| `tags` | `object` | Resource tags |
| `type` | `string` | The resource type of the dedicated HSM. |
| `zones` | `array` | The Dedicated Hsm zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets the specified Azure dedicated HSM. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | The List operation gets information about the dedicated HSMs associated with the subscription. |
| `create_or_update` | `INSERT` | `name, resourceGroupName, subscriptionId, data__location, data__properties, data__sku` | Create or Update a dedicated HSM in the specified subscription. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Deletes the specified Azure Dedicated HSM. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | The List operation gets information about the dedicated HSMs associated with the subscription. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update a dedicated HSM in the specified subscription. |
