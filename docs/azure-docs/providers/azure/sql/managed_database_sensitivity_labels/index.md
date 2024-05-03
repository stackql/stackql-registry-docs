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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_database_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.managed_database_sensitivity_labels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Resource that manages the sensitivity label. |
| <CopyableCode code="properties" /> | `object` | Properties of a sensitivity label. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName" /> | Gets the sensitivity label of a given column |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName" /> | Creates or updates the sensitivity label of a given column |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName" /> | Deletes the sensitivity label of a given column |
| <CopyableCode code="disable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName" /> | Disables sensitivity recommendations on a given column |
| <CopyableCode code="enable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, sensitivityLabelSource, subscriptionId, tableName" /> | Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns) |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="databaseName, managedInstanceName, resourceGroupName, subscriptionId" /> | Update sensitivity labels of a given database using an operations batch. |
