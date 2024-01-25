---
title: cloud_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_connectors
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
<tr><td><b>Name</b></td><td><code>cloud_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_cloud.cloud_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Cloud connector resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cloudConnectorName, resourceGroupName, subscriptionId` | Gets the specified cloud connector in a specified resource group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Return list of cloud connectors in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Return list of cloud connectors in a subscription. |
| `create_or_update` | `INSERT` | `cloudConnectorName, resourceGroupName, subscriptionId` | Creates or updates a cloud connector resource. |
| `delete` | `DELETE` | `cloudConnectorName, resourceGroupName, subscriptionId` | Deletes a specified cloud connector resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Return list of cloud connectors in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Return list of cloud connectors in a subscription. |
| `discover_resources` | `EXEC` | `cloudConnectorName, resourceGroupName, subscriptionId` | Returns a list of discovered remote cloud resources via this cloud connector resource. |
