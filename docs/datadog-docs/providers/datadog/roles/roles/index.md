---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.roles.roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique identifier of the role. |
| <CopyableCode code="attributes" /> | `object` | Attributes of the role. |
| <CopyableCode code="relationships" /> | `object` | Relationships of the role object returned by the API. |
| <CopyableCode code="type" /> | `string` | Roles type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_role" /> | `SELECT` | <CopyableCode code="role_id, dd_site" /> | Get a role in the organization specified by the role’s `role_id`. |
| <CopyableCode code="list_roles" /> | `SELECT` | <CopyableCode code="dd_site" /> | Returns all roles, including their names and their unique identifiers. |
| <CopyableCode code="create_role" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a new role for your organization. |
| <CopyableCode code="delete_role" /> | `DELETE` | <CopyableCode code="role_id, dd_site" /> | Disables a role. |
| <CopyableCode code="_get_role" /> | `EXEC` | <CopyableCode code="role_id, dd_site" /> | Get a role in the organization specified by the role’s `role_id`. |
| <CopyableCode code="_list_roles" /> | `EXEC` | <CopyableCode code="dd_site" /> | Returns all roles, including their names and their unique identifiers. |
| <CopyableCode code="clone_role" /> | `EXEC` | <CopyableCode code="role_id, data__data, dd_site" /> | Clone an existing role |
| <CopyableCode code="update_role" /> | `EXEC` | <CopyableCode code="role_id, data__data, dd_site" /> | Edit a role. Can only be used with application keys belonging to administrators. |
