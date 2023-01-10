---
title: scale_units
hide_title: false
hide_table_of_contents: false
keywords:
  - scale_units
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
<tr><td><b>Name</b></td><td><code>scale_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.fabric_admin.scale_units</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of a scale unit. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ScaleUnits_Get` | `SELECT` | `location, resourceGroupName, scaleUnit, subscriptionId` | Returns the requested scale unit. |
| `ScaleUnits_List` | `SELECT` | `location, resourceGroupName, subscriptionId` | Returns a list of all scale units at a location. |
| `ScaleUnits_CreateFromJson` | `EXEC` | `location, resourceGroupName, scaleUnit, subscriptionId` | Add a new scale unit. |
| `ScaleUnits_ScaleOut` | `EXEC` | `location, resourceGroupName, scaleUnit, subscriptionId` | Scales out a scale unit. |
| `ScaleUnits_SetGPUPartitionSize` | `EXEC` | `location, resourceGroupName, scaleUnit, subscriptionId` | Set GPU partition size. |
