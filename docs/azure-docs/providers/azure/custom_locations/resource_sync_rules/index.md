---
title: resource_sync_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_sync_rules
  - custom_locations
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
<tr><td><b>Name</b></td><td><code>resource_sync_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.custom_locations.resource_sync_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties for a resource sync rule. For an unmapped custom resource, its labels will be used to find out matching resource sync rules using the selector property of the resource sync rule. If this resource sync rule has highest priority among all matching rules, then the unmapped custom resource will be projected to the target resource group associated with this resource sync rule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | Gets the details of the resourceSyncRule with a specified resource group, subscription id Custom Location resource name and Resource Sync Rule name. |
| `list_by_custom_location_id` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Gets a list of Resource Sync Rules in the specified subscription. The operation returns properties of each Resource Sync Rule |
| `create_or_update` | `INSERT` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | Creates or updates a Resource Sync Rule in the parent Custom Location, Subscription Id and Resource Group |
| `delete` | `DELETE` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | Deletes the Resource Sync Rule with the specified Resource Sync Rule Name, Custom Location Resource Name, Resource Group, and Subscription Id. |
| `_list_by_custom_location_id` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Gets a list of Resource Sync Rules in the specified subscription. The operation returns properties of each Resource Sync Rule |
| `update` | `EXEC` | `childResourceName, resourceGroupName, resourceName, subscriptionId` | Updates a Resource Sync Rule with the specified Resource Sync Rule name in the specified Resource Group, Subscription and Custom Location name. |
