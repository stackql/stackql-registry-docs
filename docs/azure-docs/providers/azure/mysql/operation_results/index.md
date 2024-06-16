---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - mysql
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
<tr><td><b>Name</b></td><td><code>operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mysql.operation_results" /></td></tr>
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
| <CopyableCode code="properties" /> | `object` | A name-value pair that represents extended info. |
| <CopyableCode code="resourceId" /> | `string` | Fully qualified ID of the resource against which the original async operation was started. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationName, operationId, subscriptionId" /> |
