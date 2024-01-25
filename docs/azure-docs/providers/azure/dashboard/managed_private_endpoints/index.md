---
title: managed_private_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_private_endpoints
  - dashboard
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
<tr><td><b>Name</b></td><td><code>managed_private_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dashboard.managed_private_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties specific to the managed private endpoint. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName` |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `create` | `INSERT` | `managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName` |
| `delete` | `DELETE` | `managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName` |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `refresh` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
| `update` | `EXEC` | `managedPrivateEndpointName, resourceGroupName, subscriptionId, workspaceName` |
