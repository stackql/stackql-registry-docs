---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - group
  - okta    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Okta resources using SQL
custom_edit_url: null
image: /img/providers/okta/stackql-okta-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="okta.group.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="_embedded" /> | `object` |
| <CopyableCode code="_links" /> | `object` |
| <CopyableCode code="activated" /> | `string` |
| <CopyableCode code="created" /> | `string` |
| <CopyableCode code="credentials" /> | `object` |
| <CopyableCode code="lastLogin" /> | `string` |
| <CopyableCode code="lastUpdated" /> | `string` |
| <CopyableCode code="passwordChanged" /> | `string` |
| <CopyableCode code="profile" /> | `object` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="statusChanged" /> | `string` |
| <CopyableCode code="transitioningToStatus" /> | `string` |
| <CopyableCode code="type" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupId, subdomain" /> | Enumerates all users that are a member of a group. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="groupId, userId, subdomain" /> | Adds a user to a group with 'OKTA_GROUP' type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, userId, subdomain" /> | Removes a user from a group with 'OKTA_GROUP' type. |
