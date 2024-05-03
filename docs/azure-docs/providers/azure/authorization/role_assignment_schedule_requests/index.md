---
title: role_assignment_schedule_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignment_schedule_requests
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
<tr><td><b>Name</b></td><td><code>role_assignment_schedule_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_assignment_schedule_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role assignment schedule request ID. |
| <CopyableCode code="name" /> | `string` | The role assignment schedule request name. |
| <CopyableCode code="properties" /> | `object` | Role assignment schedule request properties with scope. |
| <CopyableCode code="type" /> | `string` | The role assignment schedule request type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Get the specified role assignment schedule request. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Creates a role assignment schedule request. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Cancels a pending role assignment schedule request. |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="roleAssignmentScheduleRequestName, scope" /> | Validates a new role assignment schedule request. |
