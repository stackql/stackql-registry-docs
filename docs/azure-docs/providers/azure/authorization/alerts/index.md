---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert ID. |
| <CopyableCode code="name" /> | `string` | The alert name. |
| <CopyableCode code="properties" /> | `object` | Alert properties. |
| <CopyableCode code="type" /> | `string` | The alert type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, scope" /> | Get the specified alert. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="alertId, scope" /> | Refresh an alert. |
| <CopyableCode code="refresh_all" /> | `EXEC` | <CopyableCode code="scope" /> | Refresh all alerts for a resource scope. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="alertId, scope" /> | Update an alert. |
