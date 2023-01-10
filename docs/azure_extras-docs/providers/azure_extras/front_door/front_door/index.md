---
title: front_door
hide_title: false
hide_table_of_contents: false
keywords:
  - front_door
  - front_door
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>front_door</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.front_door.front_door</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The JSON object that contains the properties required to create an endpoint. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FrontDoors_Get` | `SELECT` | `frontDoorName, resourceGroupName, subscriptionId` | Gets a Front Door with the specified Front Door name under the specified subscription and resource group. |
| `FrontDoors_List` | `SELECT` | `subscriptionId` | Lists all of the Front Doors within an Azure subscription. |
| `FrontDoors_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all of the Front Doors within a resource group under a subscription. |
| `FrontDoors_CreateOrUpdate` | `INSERT` | `frontDoorName, resourceGroupName, subscriptionId` | Creates a new Front Door with a Front Door name under the specified subscription and resource group. |
| `FrontDoors_Delete` | `DELETE` | `frontDoorName, resourceGroupName, subscriptionId` | Deletes an existing Front Door with the specified parameters. |
| `FrontDoors_ValidateCustomDomain` | `EXEC` | `frontDoorName, resourceGroupName, subscriptionId, data__hostName` | Validates the custom domain mapping to ensure it maps to the correct Front Door endpoint in DNS. |
