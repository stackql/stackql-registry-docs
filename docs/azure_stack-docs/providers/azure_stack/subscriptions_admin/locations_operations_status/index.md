---
title: locations_operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - locations_operations_status
  - subscriptions_admin
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
<tr><td><b>Name</b></td><td><code>locations_operations_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.subscriptions_admin.locations_operations_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `object` | The admin offer identifier for the location wide SubscriptionsAdminResourceTypes.OperationsStatus resource type. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | The extended error information. |
| <CopyableCode code="percentComplete" /> | `number` | The completion percentage of the operation. |
| <CopyableCode code="properties" /> | `object` | The internal operation properties. |
| <CopyableCode code="responseContent" /> | `object` | The content of the response. |
| <CopyableCode code="retryAfter" /> | `string` | The amount of time clients should wait.. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | The status of the operation. |
| <CopyableCode code="terminalHttpStatusCode" /> | `string` | The terminal http status code for the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationsStatusName, subscriptionId" /> |
