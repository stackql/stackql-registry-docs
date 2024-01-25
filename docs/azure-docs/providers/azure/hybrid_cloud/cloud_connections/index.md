---
title: cloud_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_connections
  - hybrid_cloud
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
<tr><td><b>Name</b></td><td><code>cloud_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_cloud.cloud_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Cloud connection resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudConnectionName, resourceGroupName, subscriptionId` | Gets the specified cloud connection in a specified resource group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Return list of cloud connections in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Return list of cloud connections in a subscription. |
| `create_or_update` | `INSERT` | `cloudConnectionName, resourceGroupName, subscriptionId` | Creates or updates a cloud connection resource |
| `delete` | `DELETE` | `cloudConnectionName, resourceGroupName, subscriptionId` | Deletes a specified cloud connection resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Return list of cloud connections in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Return list of cloud connections in a subscription. |
