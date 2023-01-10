---
title: scale_unit_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_unit_nodes
  - fabric_admin
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.fabric_admin.scale_unit_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Holds all properties related to a scale unit node. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScaleUnitNodes_Get` | `SELECT` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Return the requested scale unit node. |
| `ScaleUnitNodes_List` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all scale unit nodes in a location. |
| `ScaleUnitNodes_PowerOff` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Power off a scale unit node. |
| `ScaleUnitNodes_PowerOn` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Power on a scale unit node. |
| `ScaleUnitNodes_Repair` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Repairs a node of the cluster. |
| `ScaleUnitNodes_Shutdown` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Shutdown a scale unit node. |
| `ScaleUnitNodes_StartMaintenanceMode` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Start maintenance mode for a scale unit node. |
| `ScaleUnitNodes_StopMaintenanceMode` | `EXEC` | `location, resourceGroupName, scaleUnitNode, subscriptionId` | Stop maintenance mode for a scale unit node. |
