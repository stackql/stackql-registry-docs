---
title: role_assignment_schedule_instances_for_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignment_schedule_instances_for_scope
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
<tr><td><b>Name</b></td><td><code>role_assignment_schedule_instances_for_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_assignment_schedule_instances_for_scope" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role assignment schedule instance ID. |
| <CopyableCode code="name" /> | `string` | The role assignment schedule instance name. |
| <CopyableCode code="properties" /> | `object` | Role assignment schedule properties with scope. |
| <CopyableCode code="type" /> | `string` | The role assignment schedule instance type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> |
