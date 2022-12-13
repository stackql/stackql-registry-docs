---
title: volume
hide_title: false
hide_table_of_contents: false
keywords:
  - volume
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>volume</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.volume</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | This type describes properties of a volume resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Volume_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, volumeResourceName` | Gets the information about the volume resource with the given name. The information include the description and other properties of the volume. |
| `Volume_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets the information about all volume resources in a given resource group. The information include the description and other properties of the Volume. |
| `Volume_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets the information about all volume resources in a given resource group. The information include the description and other properties of the volume. |
| `Volume_Create` | `INSERT` | `api-version, resourceGroupName, subscriptionId, volumeResourceName, data__properties` | Creates a volume resource with the specified name, description and properties. If a volume resource with the same name exists, then it is updated with the specified description and properties. |
| `Volume_Delete` | `DELETE` | `api-version, resourceGroupName, subscriptionId, volumeResourceName` | Deletes the volume resource identified by the name. |
