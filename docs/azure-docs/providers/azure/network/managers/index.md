---
title: managers
hide_title: false
hide_table_of_contents: false
keywords:
  - managers
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
<tr><td><b>Name</b></td><td><code>managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.managers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of Managed Network |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkManagers_Get` | `SELECT` |  | Gets the specified Network Manager. |
| `NetworkManagers_List` | `SELECT` | `resourceGroupName, subscriptionId` | List network managers in a resource group. |
| `NetworkManagers_ListBySubscription` | `SELECT` | `subscriptionId` | List all network managers in a subscription. |
| `NetworkManagers_CreateOrUpdate` | `INSERT` |  | Creates or updates a Network Manager. |
| `NetworkManagers_Delete` | `DELETE` |  | Deletes a network manager. |
| `NetworkManagers_Patch` | `EXEC` |  | Patch NetworkManager. |
