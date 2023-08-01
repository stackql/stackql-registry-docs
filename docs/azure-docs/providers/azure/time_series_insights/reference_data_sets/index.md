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
| `ReferenceDataSets_Get` | `SELECT` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId` | Gets the reference data set with the specified name in the specified environment. |
| `ReferenceDataSets_ListByEnvironment` | `SELECT` | `environmentName, resourceGroupName, subscriptionId` | Lists all the available reference data sets associated with the subscription and within the specified resource group and environment. |
| `ReferenceDataSets_CreateOrUpdate` | `INSERT` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId, data__properties` | Create or update a reference data set in the specified environment. |
| `ReferenceDataSets_Delete` | `DELETE` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId` | Deletes the reference data set with the specified name in the specified subscription, resource group, and environment |
| `ReferenceDataSets_Update` | `EXEC` | `environmentName, referenceDataSetName, resourceGroupName, subscriptionId` | Updates the reference data set with the specified name in the specified subscription, resource group, and environment. |
