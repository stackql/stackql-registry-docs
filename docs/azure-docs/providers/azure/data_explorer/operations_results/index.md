---
title: operations_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_results
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>operations_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_explorer.operations_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="endTime" /> | `string` | The operation end time |
| <CopyableCode code="error" /> | `object` | Operation result error properties |
| <CopyableCode code="percentComplete" /> | `number` | Percentage completed. |
| <CopyableCode code="properties" /> | `object` | Operation result properties |
| <CopyableCode code="startTime" /> | `string` | The operation start time |
| <CopyableCode code="status" /> | `string` | The status of operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationId, subscriptionId" /> |
