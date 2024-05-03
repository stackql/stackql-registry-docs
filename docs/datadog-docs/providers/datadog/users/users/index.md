---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.users.users" /></td></tr>
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
| <CopyableCode code="get_user" /> | `SELECT` | <CopyableCode code="user_id, dd_site" /> | Get a user in the organization specified by the user’s `user_id`. |
| <CopyableCode code="list_users" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get the list of all users in the organization. This list includes<br />all users even if they are deactivated or unverified. |
| <CopyableCode code="create_user" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a user for your organization. |
| <CopyableCode code="_get_user" /> | `EXEC` | <CopyableCode code="user_id, dd_site" /> | Get a user in the organization specified by the user’s `user_id`. |
| <CopyableCode code="_list_users" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get the list of all users in the organization. This list includes<br />all users even if they are deactivated or unverified. |
| <CopyableCode code="disable_user" /> | `EXEC` | <CopyableCode code="user_id, dd_site" /> | Disable a user. Can only be used with an application key belonging<br />to an administrator user. |
| <CopyableCode code="update_user" /> | `EXEC` | <CopyableCode code="user_id, data__data, dd_site" /> | Edit a user. Can only be used with an application key belonging<br />to an administrator user. |
