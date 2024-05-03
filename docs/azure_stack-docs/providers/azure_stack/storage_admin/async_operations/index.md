---
title: async_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - async_operations
  - storage_admin
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>async_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.storage_admin.async_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation id. |
| <CopyableCode code="context" /> | `object` | Operation request context. |
| <CopyableCode code="httpStatus" /> | `string` | Http status for the async operation. |
| <CopyableCode code="locationHeader" /> | `string` | Location header for async operation. |
| <CopyableCode code="operation" /> | `object` | Async operation content |
| <CopyableCode code="operationEndTime" /> | `string` | Operation end time. |
| <CopyableCode code="operationStartTime" /> | `string` | Operation start time. |
| <CopyableCode code="response" /> | `string` | Response for the async operation. |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription id for async operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="asyncOperationId, location, subscriptionId" /> |
