---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
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
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role assignment ID. |
| <CopyableCode code="name" /> | `string` | The role assignment name. |
| <CopyableCode code="properties" /> | `object` | Role assignment properties. |
| <CopyableCode code="type" /> | `string` | The role assignment type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleAssignmentName, scope" /> | Get a role assignment by scope and name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="roleAssignmentName, scope, data__properties" /> | Create or update a role assignment by scope and name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="roleAssignmentName, scope" /> | Delete a role assignment by scope and name. |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="roleAssignmentId" /> | Delete a role assignment by ID. |
| <CopyableCode code="create_by_id" /> | `EXEC` | <CopyableCode code="roleAssignmentId, data__properties" /> | Create or update a role assignment by ID. |
| <CopyableCode code="get_by_id" /> | `EXEC` | <CopyableCode code="roleAssignmentId" /> | Get a role assignment by ID. |
