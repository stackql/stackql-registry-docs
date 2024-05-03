---
title: workload_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_classifiers
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
<tr><td><b>Name</b></td><td><code>workload_classifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.workload_classifiers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName" /> | Gets a workload classifier |
| <CopyableCode code="list_by_workload_group" /> | `SELECT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName" /> | Gets the list of workload classifiers for a workload group |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName" /> | Creates or updates a workload classifier. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName" /> | Deletes a workload classifier. |
| <CopyableCode code="_list_by_workload_group" /> | `EXEC` | <CopyableCode code="databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName" /> | Gets the list of workload classifiers for a workload group |
