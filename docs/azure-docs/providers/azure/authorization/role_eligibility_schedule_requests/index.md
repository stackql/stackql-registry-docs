---
title: role_eligibility_schedule_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - role_eligibility_schedule_requests
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
<tr><td><b>Name</b></td><td><code>role_eligibility_schedule_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_eligibility_schedule_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role eligibility schedule request ID. |
| <CopyableCode code="name" /> | `string` | The role eligibility schedule request name. |
| <CopyableCode code="properties" /> | `object` | Role eligibility schedule request properties with scope. |
| <CopyableCode code="type" /> | `string` | The role eligibility schedule request type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleEligibilityScheduleRequestName, scope" /> | Get the specified role eligibility schedule request. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="roleEligibilityScheduleRequestName, scope" /> | Creates a role eligibility schedule request. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="roleEligibilityScheduleRequestName, scope" /> | Cancels a pending role eligibility schedule request. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="roleEligibilityScheduleRequestName, scope" /> | Validates a new role eligibility schedule request. |
