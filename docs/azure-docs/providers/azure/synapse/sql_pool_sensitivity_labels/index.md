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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sql_pool_sensitivity_labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_sensitivity_labels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | managed by |
| <CopyableCode code="properties" /> | `object` | Properties of a sensitivity label. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Gets the sensitivity label of a given column |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Creates or updates the sensitivity label of a given column in a Sql pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Deletes the sensitivity label of a given column in a Sql pool |
| <CopyableCode code="disable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Disables sensitivity recommendations on a given column |
| <CopyableCode code="enable_recommendation" /> | `EXEC` | <CopyableCode code="columnName, resourceGroupName, schemaName, sensitivityLabelSource, sqlPoolName, subscriptionId, tableName, workspaceName" /> | Enables sensitivity recommendations on a given column (recommendations are enabled by default on all columns) |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Update sensitivity labels of a given SQL Pool using an operations batch. |
