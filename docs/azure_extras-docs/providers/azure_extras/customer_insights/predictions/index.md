---
title: predictions
hide_title: false
hide_table_of_contents: false
keywords:
  - predictions
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>predictions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.predictions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The prediction definition. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hubName, predictionName, resourceGroupName, subscriptionId` | Gets a Prediction in the hub. |
| `list_by_hub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all the predictions in the specified hub. |
| `create_or_update` | `INSERT` | `hubName, predictionName, resourceGroupName, subscriptionId` | Creates a Prediction or updates an existing Prediction in the hub. |
| `delete` | `DELETE` | `hubName, predictionName, resourceGroupName, subscriptionId` | Deletes a Prediction in the hub. |
| `_list_by_hub` | `EXEC` | `hubName, resourceGroupName, subscriptionId` | Gets all the predictions in the specified hub. |
| `model_status` | `EXEC` | `hubName, predictionName, resourceGroupName, subscriptionId, data__status` | Creates or updates the model status of prediction. |
