---
title: managed_database_sensitivity_labels
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_sensitivity_labels
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_database_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_sensitivity_labels</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedBy` | `string` | Resource that manages the sensitivity label. |
| `properties` | `object` | Properties of a sensitivity label. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName` | Gets the sensitivity label of a given column |
| `create_or_update` | `INSERT` | `columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName` | Creates or updates the sensitivity label of a given column |
| `delete` | `DELETE` | `columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName` | Deletes the sensitivity label of a given column |
| `disable_recommendation` | `EXEC` | `columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName` | Disables sensitivity recommendations on a given column |
| `enable_recommendation` | `EXEC` | `columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName` | Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns) |
| `update` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Update sensitivity labels of a given database using an operations batch. |
