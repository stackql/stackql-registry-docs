---
title: sql_pool_restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_restore_points
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
<tr><td><b>Name</b></td><td><code>sql_pool_restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.sql_pool_restore_points" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of a database restore point |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, restorePointName, sqlPoolName, subscriptionId, workspaceName" /> | Gets a restore point. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get SQL pool backup information |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__restorePointLabel" /> | Creates a restore point for a data warehouse. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, restorePointName, sqlPoolName, subscriptionId, workspaceName" /> | Deletes a restore point. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Get SQL pool backup information |
