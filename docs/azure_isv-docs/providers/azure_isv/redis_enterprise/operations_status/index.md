---
title: operations_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_status
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>operations_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis_enterprise.operations_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The operation's unique id. |
| <CopyableCode code="name" /> | `string` | The operation's name. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | Common error response for all Azure Resource Manager APIs to return error details for failed operations. (This also follows the OData error response format.). |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | The current status of the operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationId, subscriptionId" /> |
