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
| `resources` | `array` | The list of extensions affiliated to the machine |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a hybrid machine. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Machines_Get` | `SELECT` | `machineName, resourceGroupName, subscriptionId` | Retrieves information about the model view or the instance view of a hybrid machine. |
| `Machines_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines. |
| `Machines_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines. |
| `Machines_CreateOrUpdate` | `INSERT` | `machineName, resourceGroupName, subscriptionId` | The operation to create or update a hybrid machine. Please note some properties can be set only during machine creation. |
| `Machines_Delete` | `DELETE` | `machineName, resourceGroupName, subscriptionId` | The operation to delete a hybrid machine. |
| `Machines_Update` | `EXEC` | `machineName, resourceGroupName, subscriptionId` | The operation to update a hybrid machine. |
