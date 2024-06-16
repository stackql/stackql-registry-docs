---
title: alert_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_incidents
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
<tr><td><b>Name</b></td><td><code>alert_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.alert_incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The alert incident ID. |
| <CopyableCode code="name" /> | `string` | The alert incident name. |
| <CopyableCode code="properties" /> | `object` | Alert incident properties |
| <CopyableCode code="type" /> | `string` | The alert incident type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="alertId, alertIncidentId, scope" /> | Get the specified alert incident. |
| <CopyableCode code="remediate" /> | `EXEC` | <CopyableCode code="alertId, alertIncidentId, scope" /> | Remediate an alert incident. |
