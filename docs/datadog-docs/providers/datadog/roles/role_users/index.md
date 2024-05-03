---
title: role_users
hide_title: false
hide_table_of_contents: false
keywords:
  - role_users
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
<tr><td><b>Name</b></td><td><code>role_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.roles.role_users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the user. |
| <CopyableCode code="attributes" /> | `object` | Attributes of user object returned by the API. |
| <CopyableCode code="relationships" /> | `object` | Relationships of the user object returned by the API. |
| <CopyableCode code="type" /> | `string` | Users resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_role_users" /> | `SELECT` | <CopyableCode code="role_id, dd_site" /> | Gets all users of a role. |
| <CopyableCode code="remove_user_from_role" /> | `DELETE` | <CopyableCode code="role_id, data__data, dd_site" /> | Removes a user from a role. |
| <CopyableCode code="_list_role_users" /> | `EXEC` | <CopyableCode code="role_id, dd_site" /> | Gets all users of a role. |
| <CopyableCode code="add_user_to_role" /> | `EXEC` | <CopyableCode code="role_id, data__data, dd_site" /> | Adds a user to a role. |
