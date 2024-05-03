---
title: operations_azure_async_header_result
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_azure_async_header_result
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
<tr><td><b>Name</b></td><td><code>operations_azure_async_header_result</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.operations_azure_async_header_result" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Operation ID |
| <CopyableCode code="name" /> | `string` | Operation name |
| <CopyableCode code="endTime" /> | `string` | Operation start time |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="percentComplete" /> | `number` | Completion percentage of the operation |
| <CopyableCode code="properties" /> | `object` | Operation properties |
| <CopyableCode code="startTime" /> | `string` | Operation start time |
| <CopyableCode code="status" /> | `string` | Operation status |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, workspaceName" /> |
