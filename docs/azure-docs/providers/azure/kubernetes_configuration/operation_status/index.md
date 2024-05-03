---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
  - kubernetes_configuration
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
<tr><td><b>Name</b></td><td><code>operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the async operation. |
| <CopyableCode code="name" /> | `string` | Name of the async operation. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="operations" /> | `array` | The operations list. |
| <CopyableCode code="percentComplete" /> | `number` | Percent of the operation that is complete. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, operationId, resourceGroupName, subscriptionId" /> | Get Async Operation status |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List Async Operations, currently in progress, in a cluster |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List Async Operations, currently in progress, in a cluster |
