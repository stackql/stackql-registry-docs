---
title: community_trainings
hide_title: false
hide_table_of_contents: false
keywords:
  - community_trainings
  - community_training
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
<tr><td><b>Name</b></td><td><code>community_trainings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.community_training.community_trainings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Details of the Community CommunityTraining. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `communityTrainingName, resourceGroupName, subscriptionId` | Get a CommunityTraining |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List CommunityTraining resources by resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List CommunityTraining resources by subscription ID |
| `create` | `INSERT` | `communityTrainingName, resourceGroupName, subscriptionId` | Create a CommunityTraining |
| `delete` | `DELETE` | `communityTrainingName, resourceGroupName, subscriptionId` | Delete a CommunityTraining |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List CommunityTraining resources by resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List CommunityTraining resources by subscription ID |
| `update` | `EXEC` | `communityTrainingName, resourceGroupName, subscriptionId` | Update a CommunityTraining |
