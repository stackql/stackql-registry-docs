---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
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
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.users.invitations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the user invitation. |
| <CopyableCode code="attributes" /> | `object` | Attributes of a user invitation. |
| <CopyableCode code="relationships" /> | `object` | Relationships data for user invitation. |
| <CopyableCode code="type" /> | `string` | User invitations type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_invitation" /> | `SELECT` | <CopyableCode code="user_invitation_uuid, dd_site" /> | Returns a single user invitation by its UUID. |
| <CopyableCode code="_get_invitation" /> | `EXEC` | <CopyableCode code="user_invitation_uuid, dd_site" /> | Returns a single user invitation by its UUID. |
| <CopyableCode code="send_invitations" /> | `EXEC` | <CopyableCode code="data__data, dd_site" /> | Sends emails to one or more users inviting them to join the organization. |
