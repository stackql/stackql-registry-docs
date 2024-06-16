---
title: alert_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_operation
  - authorization
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
<tr><td><b>Name</b></td><td><code>alert_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_operation" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the alert operation. |
| <CopyableCode code="createdDateTime" /> | `string` | The created date of the alert operation. |
| <CopyableCode code="lastActionDateTime" /> | `string` | The last action date of the alert operation. |
| <CopyableCode code="resourceLocation" /> | `string` | The location of the alert associated with the operation. |
| <CopyableCode code="status" /> | `string` | The status of the alert operation. |
| <CopyableCode code="statusDetail" /> | `string` | The status detail of the alert operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, scope" /> |
