---
title: role_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_permissions
  - roles
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.roles.role_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the permission. |
| <CopyableCode code="attributes" /> | `object` | Attributes of a permission. |
| <CopyableCode code="type" /> | `string` | Permissions resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_role_permissions" /> | `SELECT` | <CopyableCode code="role_id, dd_site" /> | Returns a list of all permissions for a single role. |
| <CopyableCode code="remove_permission_from_role" /> | `DELETE` | <CopyableCode code="role_id, dd_site" /> | Removes a permission from a role. |
| <CopyableCode code="_list_role_permissions" /> | `EXEC` | <CopyableCode code="role_id, dd_site" /> | Returns a list of all permissions for a single role. |
| <CopyableCode code="add_permission_to_role" /> | `EXEC` | <CopyableCode code="role_id, dd_site" /> | Adds a permission to a role. |
