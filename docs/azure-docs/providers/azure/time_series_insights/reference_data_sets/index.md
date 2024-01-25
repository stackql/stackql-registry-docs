---
title: reference_data_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - reference_data_sets
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>reference_data_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.time_series_insights.reference_data_sets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location |
| `properties` | `object` | Properties of the reference data set. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId` | Gets the reference data set with the specified name in the specified environment. |
| `list_by_environment` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` | Lists all the available reference data sets associated with the subscription and within the specified resource group and environment. |
| `create_or_update` | `INSERT` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId, data__properties` | Create or update a reference data set in the specified environment. |
| `delete` | `DELETE` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId` | Deletes the reference data set with the specified name in the specified subscription, resource group, and environment |
| `_list_by_environment` | `EXEC` | `environmentName, resourceGroupName, subscriptionId` | Lists all the available reference data sets associated with the subscription and within the specified resource group and environment. |
| `update` | `EXEC` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId` | Updates the reference data set with the specified name in the specified subscription, resource group, and environment. |
