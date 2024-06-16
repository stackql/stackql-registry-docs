---
title: validate_operation_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - validate_operation_statuses
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>validate_operation_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.validate_operation_statuses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the operation. |
| <CopyableCode code="name" /> | `string` | Name of the operation. |
| <CopyableCode code="endTime" /> | `string` | Operation end time. Format: ISO-8601. |
| <CopyableCode code="error" /> | `object` | Error information associated with operation status call. |
| <CopyableCode code="properties" /> | `object` | Base class for additional information of operation status. |
| <CopyableCode code="startTime" /> | `string` | Operation start time. Format: ISO-8601. |
| <CopyableCode code="status" /> | `string` | Operation status. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, operationId, resourceGroupName, subscriptionId, vaultName" /> |
