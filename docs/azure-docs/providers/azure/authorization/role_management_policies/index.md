---
title: role_management_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - role_management_policies
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
<tr><td><b>Name</b></td><td><code>role_management_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_management_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role management policy Id. |
| <CopyableCode code="name" /> | `string` | The role management policy name. |
| <CopyableCode code="properties" /> | `object` | Role management policy properties with scope. |
| <CopyableCode code="type" /> | `string` | The role management policy type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleManagementPolicyName, scope" /> | Get the specified role management policy for a resource scope |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="roleManagementPolicyName, scope" /> | Delete a role management policy |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="roleManagementPolicyName, scope" /> | Update a role management policy |
