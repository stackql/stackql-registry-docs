---
title: farm_beats_models
hide_title: false
hide_table_of_contents: false
keywords:
  - farm_beats_models
  - ag_food_platform
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
<tr><td><b>Name</b></td><td><code>farm_beats_models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ag_food_platform.farm_beats_models</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | FarmBeats ARM Resource properties. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Identity for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FarmBeatsModels_Get` | `SELECT` | `farmBeatsResourceName, resourceGroupName, subscriptionId` | Get FarmBeats resource. |
| `FarmBeatsModels_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the FarmBeats instances for a resource group. |
| `FarmBeatsModels_ListBySubscription` | `SELECT` | `subscriptionId` | Lists the FarmBeats instances for a subscription. |
| `FarmBeatsModels_CreateOrUpdate` | `INSERT` | `farmBeatsResourceName, resourceGroupName, subscriptionId` | Create or update FarmBeats resource. |
| `FarmBeatsModels_Delete` | `DELETE` | `farmBeatsResourceName, resourceGroupName, subscriptionId` | Delete a FarmBeats resource. |
| `FarmBeatsModels_GetOperationResult` | `EXEC` | `farmBeatsResourceName, operationResultsId, resourceGroupName, subscriptionId` | Get operationResults for a FarmBeats resource. |
| `FarmBeatsModels_Update` | `EXEC` | `farmBeatsResourceName, resourceGroupName, subscriptionId` | Update a FarmBeats resource. |
