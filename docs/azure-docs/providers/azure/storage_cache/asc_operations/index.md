---
title: asc_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - asc_operations
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>asc_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.asc_operations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation Id. |
| <CopyableCode code="name" /> | `string` | The operation name. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | Describes the format of Error response. |
| <CopyableCode code="properties" /> | `object` | Additional operation-specific output. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | The status of the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationId, subscriptionId" /> |
