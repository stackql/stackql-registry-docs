---
title: grant_options
hide_title: false
hide_table_of_contents: false
keywords:
  - grant_options
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

Creates, updates, deletes, gets or lists a <code>grant_options</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grant_options</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.grant.grant_options" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="revoke_group_privilege_grant_option" /> | `DELETE` | <CopyableCode code="bulkGrantType, granteeName, granteeType, privilege, scopeName, scopeType, securableTypePlural, endpoint" /> | Endpoint to indicate that the grant option for the privilege listed on the group securable in the given scope should be revoked. |
| <CopyableCode code="revoke_privilege_grant_option" /> | `DELETE` | <CopyableCode code="granteeName, granteeType, privilege, securableName, securableType, endpoint" /> | Endpoint to indicate that the grant option for the privilege listed in the path should be revoked. |

## `DELETE` example

Deletes the specified <code>grant_options</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.grant.grant_options
WHERE granteeName = '{ granteeName }' AND granteeType = '{ granteeType }' AND privilege = '{ privilege }' AND securableName = '{ securableName }' AND securableType = '{ securableType }' AND endpoint = '{ endpoint }';
```
