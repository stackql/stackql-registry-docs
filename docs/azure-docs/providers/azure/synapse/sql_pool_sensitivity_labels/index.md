---
title: sql_pool_sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_sensitivity_labels
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_sensitivity_labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedBy` | `string` | managed by |
| `properties` | `object` | Properties of a sensitivity label. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolSensitivityLabels_Get` | `SELECT` | `columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName` | Gets the sensitivity label of a given column |
| `SqlPoolSensitivityLabels_CreateOrUpdate` | `INSERT` | `columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName` | Creates or updates the sensitivity label of a given column in a Sql pool |
| `SqlPoolSensitivityLabels_Delete` | `DELETE` | `columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName` | Deletes the sensitivity label of a given column in a Sql pool |
| `SqlPoolSensitivityLabels_DisableRecommendation` | `EXEC` | `columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName` | Disables sensitivity recommendations on a given column |
| `SqlPoolSensitivityLabels_EnableRecommendation` | `EXEC` | `columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName` | Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns) |
| `SqlPoolSensitivityLabels_ListCurrent` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Gets SQL pool sensitivity labels. |
| `SqlPoolSensitivityLabels_ListRecommended` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Gets sensitivity labels of a given SQL pool. |
| `SqlPoolSensitivityLabels_Update` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Update sensitivity labels of a given SQL Pool using an operations batch. |
