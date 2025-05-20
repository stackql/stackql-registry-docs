---
title: privileges
hide_title: false
hide_table_of_contents: false
keywords:
  - privileges
  - grant
  - snowflake
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage snowflake resources using SQL
custom_edit_url: null
image: /img/providers/snowflake/stackql-snowflake-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>privileges</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>privileges</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.grant.privileges" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="grant_group_privilege" /> | `INSERT` | <CopyableCode code="bulkGrantType, granteeName, granteeType, scopeName, scopeType, securableTypePlural, endpoint" /> | Endpoint to indicate that the privileges listed in the request body should be granted to all securables of this type in the given scope. |
| <CopyableCode code="grant_privilege" /> | `INSERT` | <CopyableCode code="granteeName, granteeType, securableName, securableType, endpoint" /> | Endpoint to indicate that the privileges listed in the request body should be granted. |
| <CopyableCode code="revoke_group_privilege" /> | `DELETE` | <CopyableCode code="bulkGrantType, granteeName, granteeType, privilege, scopeName, scopeType, securableTypePlural, endpoint" /> | Endpoint to indicate that the privilege listed on the group securable in the given scope should be revoked. |
| <CopyableCode code="revoke_privilege" /> | `DELETE` | <CopyableCode code="granteeName, granteeType, privilege, securableName, securableType, endpoint" /> | Endpoint to indicate that the privilege listed in the path should be revoked. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>privileges</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.grant.privileges (
granteeName,
endpoint,
granteeType,
securableType,
securableName
)
SELECT 
'{ granteeName }',
'{ endpoint }',
'{ securableType }',
'{ granteeType }',
'{ securableName }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: privileges
  props:
  - name: granteeName
    value: string
  - name: granteeType
    value: string
  - name: securableName
    value: string
  - name: securableType
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>privileges</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.grant.privileges
WHERE granteeName = '{ granteeName }' AND granteeType = '{ granteeType }' AND privilege = '{ privilege }' AND securableName = '{ securableName }' AND securableType = '{ securableType }' AND endpoint = '{ endpoint }';
```
