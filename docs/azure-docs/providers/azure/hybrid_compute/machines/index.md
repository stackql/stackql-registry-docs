---
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
  - hybrid_compute
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
<tr><td><b>Name</b></td><td><code>machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_compute.machines</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | Indicates which kind of Arc machine placement on-premises, such as HCI, SCVMM or VMware etc. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a hybrid machine. |
| `resources` | `array` | The list of extensions affiliated to the machine |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | Retrieves information about the model view or the instance view of a hybrid machine. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines. |
| `create_or_update` | `INSERT` | `machineName, resourceGroupName, subscriptionId` | The operation to create or update a hybrid machine. Please note some properties can be set only during machine creation. |
| `delete` | `DELETE` | `machineName, resourceGroupName, subscriptionId` | The operation to delete a hybrid machine. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines. |
| `assess_patches` | `EXEC` | `name, resourceGroupName, subscriptionId` | The operation to assess patches on a hybrid machine identity in Azure. |
| `install_patches` | `EXEC` | `name, resourceGroupName, subscriptionId, data__maximumDuration, data__rebootSetting` | The operation to install patches on a hybrid machine identity in Azure. |
| `update` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | The operation to update a hybrid machine. |
