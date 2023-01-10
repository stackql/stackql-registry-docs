---
title: custom_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_locations
  - custom_locations
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
<tr><td><b>Name</b></td><td><code>custom_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.custom_locations.custom_locations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties for a custom location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomLocations_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets the details of the customLocation with a specified resource group and name. |
| `CustomLocations_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of Custom Locations in the specified subscription and resource group. The operation returns properties of each Custom Location. |
| `CustomLocations_ListBySubscription` | `SELECT` | `subscriptionId` | Gets a list of Custom Locations in the specified subscription. The operation returns properties of each Custom Location |
| `CustomLocations_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Creates or updates a Custom Location in the specified Subscription and Resource Group |
| `CustomLocations_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Deletes the Custom Location with the specified Resource Name, Resource Group, and Subscription Id. |
| `CustomLocations_FindTargetResourceGroup` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Returns the target resource group associated with the resource sync rules of the Custom Location that match the rules passed in with the Find Target Resource Group Request. |
| `CustomLocations_ListEnabledResourceTypes` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets the list of the Enabled Resource Types. |
| `CustomLocations_ListOperations` | `EXEC` |  | Lists all available Custom Locations operations. |
| `CustomLocations_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Updates a Custom Location with the specified Resource Name in the specified Resource Group and Subscription. |
