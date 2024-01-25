---
title: appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances
  - resource_connector
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
<tr><td><b>Name</b></td><td><code>appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resource_connector.appliances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties for an appliance. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets the details of an Appliance with a specified resource group and name. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Appliances in the specified subscription and resource group. The operation returns properties of each Appliance. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets a list of Appliances in the specified subscription. The operation returns properties of each Appliance |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates or updates an Appliance in the specified Subscription and Resource Group. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes an Appliance with the specified Resource Name, Resource Group, and Subscription Id. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of Appliances in the specified subscription and resource group. The operation returns properties of each Appliance. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets a list of Appliances in the specified subscription. The operation returns properties of each Appliance |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates an Appliance with the specified Resource Name in the specified Resource Group and Subscription. |
