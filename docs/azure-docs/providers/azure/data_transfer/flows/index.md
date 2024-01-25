---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
  - data_transfer
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
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_transfer.flows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `plan` | `object` | Plan for the resource. |
| `properties` | `object` | Properties of flow |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionName, flowName, resourceGroupName, subscriptionId` | Gets flow resource. |
| `list_by_connection` | `SELECT` | `connectionName, resourceGroupName, subscriptionId` | Gets flows in a connection. |
| `create_or_update` | `INSERT` | `connectionName, flowName, resourceGroupName, subscriptionId, data__location` | Creates or updates the flow resource. |
| `delete` | `DELETE` | `connectionName, flowName, resourceGroupName, subscriptionId` | Deletes the flow resource. |
| `_list_by_connection` | `EXEC` | `connectionName, resourceGroupName, subscriptionId` | Gets flows in a connection. |
| `disable` | `EXEC` | `connectionName, flowName, resourceGroupName, subscriptionId` | Disables the specified flow |
| `enable` | `EXEC` | `connectionName, flowName, resourceGroupName, subscriptionId` | Enables the specified flow. |
| `link` | `EXEC` | `connectionName, flowName, resourceGroupName, subscriptionId, data__id` | Links the specified flow. |
| `update` | `EXEC` | `connectionName, flowName, resourceGroupName, subscriptionId` | Updates the flow resource. |
