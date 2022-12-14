---
title: virtual_wans
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_wans
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_wans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_wans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Parameters for VirtualWAN. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualWans_Get` | `SELECT` | `VirtualWANName, resourceGroupName, subscriptionId` | Retrieves the details of a VirtualWAN. |
| `VirtualWans_List` | `SELECT` | `subscriptionId` | Lists all the VirtualWANs in a subscription. |
| `VirtualWans_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the VirtualWANs in a resource group. |
| `VirtualWans_CreateOrUpdate` | `INSERT` | `VirtualWANName, resourceGroupName, subscriptionId, data__location` | Creates a VirtualWAN resource if it doesn't exist else updates the existing VirtualWAN. |
| `VirtualWans_Delete` | `DELETE` | `VirtualWANName, resourceGroupName, subscriptionId` | Deletes a VirtualWAN. |
| `VirtualWans_UpdateTags` | `EXEC` | `VirtualWANName, resourceGroupName, subscriptionId` | Updates a VirtualWAN tags. |
