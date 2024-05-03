---
title: request_status
hide_title: false
hide_table_of_contents: false
keywords:
  - request_status
  - quota
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
<tr><td><b>Name</b></td><td><code>request_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.quota.request_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Quota request ID. |
| <CopyableCode code="name" /> | `string` | Quota request name. |
| <CopyableCode code="properties" /> | `object` | Quota request properties. |
| <CopyableCode code="type" /> | `string` | Resource type. "Microsoft.Quota/quotas". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, scope" /> | Get the quota request details and status by quota request ID for the resources of the resource provider at a specific location. The quota request ID **id** is returned in the response of the PUT operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | For the specified scope, get the current quota requests for a one year period ending at the time is made. Use the **oData** filter to select quota requests. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="scope" /> | For the specified scope, get the current quota requests for a one year period ending at the time is made. Use the **oData** filter to select quota requests. |
