---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - users
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.users.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique identifier for the user. |
| <CopyableCode code="createdAt" /> | `string` | Creation timestamp in UTC in [RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="createdBy" /> | `string` | Identifier of the user who created the resource. |
| <CopyableCode code="email" /> | `string` | Email address of the user. |
| <CopyableCode code="firstName" /> | `string` | First name of the user. |
| <CopyableCode code="isActive" /> | `boolean` | True if the user is active. |
| <CopyableCode code="isLocked" /> | `boolean` | This has the value `true` if the user's account has been locked. If a user tries to log into their account several times and fails, his or her account will be locked for security reasons. |
| <CopyableCode code="isMfaEnabled" /> | `boolean` | True if multi factor authentication is enabled for the user. |
| <CopyableCode code="lastLoginTimestamp" /> | `string` | Timestamp of the last login for the user in UTC. Will be null if the user has never logged in. |
| <CopyableCode code="lastName" /> | `string` | Last name of the user. |
| <CopyableCode code="modifiedAt" /> | `string` | Last modification timestamp in UTC. |
| <CopyableCode code="modifiedBy" /> | `string` | Identifier of the user who last modified the resource. |
| <CopyableCode code="roleIds" /> | `array` | List of roleIds associated with the user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getUser" /> | `SELECT` | <CopyableCode code="id, region" /> | Get a user with the given identifier from the organization. |
| <CopyableCode code="listUsers" /> | `SELECT` | <CopyableCode code="region" /> | Get a list of all users in the organization. The response is paginated with a default limit of 100 users per page. |
| <CopyableCode code="createUser" /> | `INSERT` | <CopyableCode code="data__email, data__firstName, data__lastName, data__roleIds, region" /> | Create a new user in the organization. |
| <CopyableCode code="deleteUser" /> | `DELETE` | <CopyableCode code="id, region" /> | Delete a user with the given identifier from the organization and transfer their content to the user with the identifier specified in "transferTo". |
| <CopyableCode code="updateUser" /> | `EXEC` | <CopyableCode code="id, data__firstName, data__isActive, data__lastName, data__roleIds, region" /> | Update an existing user in the organization. |
