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
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of Managed Network |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets the specified Network Manager. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | List network managers in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all network managers in a subscription. |
| `create_or_update` | `INSERT` |  | Creates or updates a Network Manager. |
| `delete` | `DELETE` |  | Deletes a network manager. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | List network managers in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all network managers in a subscription. |
| `patch` | `EXEC` |  | Patch NetworkManager. |
