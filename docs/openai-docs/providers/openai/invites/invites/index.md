---
title: invites
hide_title: false
hide_table_of_contents: false
keywords:
  - invites
  - invites
  - openai
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage openai resources using SQL
custom_edit_url: null
image: /img/providers/openai/stackql-openai-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>invites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="openai.invites.invites" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier, which can be referenced in API endpoints |
| <CopyableCode code="accepted_at" /> | `integer` | The Unix timestamp (in seconds) of when the invite was accepted. |
| <CopyableCode code="email" /> | `string` | The email address of the individual to whom the invite was sent |
| <CopyableCode code="expires_at" /> | `integer` | The Unix timestamp (in seconds) of when the invite expires. |
| <CopyableCode code="invited_at" /> | `integer` | The Unix timestamp (in seconds) of when the invite was sent. |
| <CopyableCode code="object" /> | `string` | The object type, which is always `organization.invite` |
| <CopyableCode code="role" /> | `string` | `owner` or `reader` |
| <CopyableCode code="status" /> | `string` | `accepted`,`expired`, or `pending` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_invites" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="retrieve_invite" /> | `SELECT` | <CopyableCode code="invite_id" /> |  |
| <CopyableCode code="delete_invite" /> | `DELETE` | <CopyableCode code="invite_id" /> |  |

## `SELECT` examples




```sql
SELECT
id,
accepted_at,
email,
expires_at,
invited_at,
object,
role,
status
FROM openai.invites.invites
;
```
## `DELETE` example

Deletes the specified <code>invites</code> resource.

```sql
/*+ delete */
DELETE FROM openai.invites.invites
WHERE invite_id = '{{ invite_id }}';
```
