---
title: scale_unit_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_unit_nodes
  - fabric_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>scale_unit_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.fabric_admin.scale_unit_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | URI of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | The region where the resource is located. |
| `properties` | `object` | Holds all properties related to a scale unit node. |
| `tags` | `object` | List of key-value pairs. |
| `type` | `string` | Type of resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Return the requested scale unit node. |
| `list` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all scale unit nodes in a location. |
| `_list` | `EXEC` | `location, resourceGroupName, subscriptionId` | Returns a list of all scale unit nodes in a location. |
| `power_off` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Power off a scale unit node. |
| `power_on` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Power on a scale unit node. |
| `repair` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Repairs a node of the cluster. |
| `shutdown` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Shutdown a scale unit node. |
| `start_maintenance_mode` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Start maintenance mode for a scale unit node. |
| `stop_maintenance_mode` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Stop maintenance mode for a scale unit node. |
