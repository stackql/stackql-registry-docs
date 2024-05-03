---
title: operation_status_resource_group_context
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status_resource_group_context
  - data_protection
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
<tr><td><b>Name</b></td><td><code>operation_status_resource_group_context</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.operation_status_resource_group_context" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | It should match what is used to GET the operation result |
| <CopyableCode code="name" /> | `string` | It must match the last segment of the "id" field, and will typically be a GUID / system generated value |
| <CopyableCode code="endTime" /> | `string` | End time of the operation |
| <CopyableCode code="error" /> | `object` | The resource management error response. |
| <CopyableCode code="properties" /> | `object` | Operation Extended Info |
| <CopyableCode code="startTime" /> | `string` | Start time of the operation |
| <CopyableCode code="status" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId" /> |
