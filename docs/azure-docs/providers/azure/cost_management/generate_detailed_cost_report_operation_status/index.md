---
title: generate_detailed_cost_report_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - generate_detailed_cost_report_operation_status
  - cost_management
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
<tr><td><b>Name</b></td><td><code>generate_detailed_cost_report_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.generate_detailed_cost_report_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the long running operation. |
| <CopyableCode code="name" /> | `string` | The name of the long running operation. |
| <CopyableCode code="endTime" /> | `string` | The endTime of the operation. |
| <CopyableCode code="error" /> | `object` | The details of the error. |
| <CopyableCode code="properties" /> | `object` | The URL to download the generated report. |
| <CopyableCode code="startTime" /> | `string` | The startTime of the operation. |
| <CopyableCode code="status" /> | `object` | The status of the long running operation. |
| <CopyableCode code="type" /> | `string` | The type of the long running operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, scope" /> |
