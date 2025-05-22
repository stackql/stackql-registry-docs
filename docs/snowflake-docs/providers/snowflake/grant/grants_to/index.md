---
title: grants_to
hide_title: false
hide_table_of_contents: false
keywords:
  - grants_to
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

Creates, updates, deletes, gets or lists a <code>grants_to</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants_to</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.grant.grants_to" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_on" /> | `string` |  |
| <CopyableCode code="grant_option" /> | `boolean` | Can grantee pass this privilege down? |
| <CopyableCode code="granted_by_name" /> | `string` | The role that granted this privilege to this grantee |
| <CopyableCode code="granted_by_role_type" /> | `string` | Type of role that granted this privilege to this grantee |
| <CopyableCode code="grantee_name" /> | `string` | Specific name of object being granted to |
| <CopyableCode code="grantee_type" /> | `string` | Entity type being granted to |
| <CopyableCode code="privileges" /> | `array` | Privilege type |
| <CopyableCode code="securable_name" /> | `string` | Name of specific object granted on (not name of privilege!) |
| <CopyableCode code="securable_type" /> | `string` | Type of object granted on |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_grants_to" /> | `SELECT` | <CopyableCode code="granteeName, granteeType, endpoint" /> | <CopyableCode code="showLimit" /> | List the roles and privileges granted to the specified grantee using the output of SHOW GRANTS TO |
<br />
Expand this to view optional parameter details for all methods in this resource.


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |

</details>

## `SELECT` examples

List the roles and privileges granted to the specified grantee using the output of SHOW GRANTS TO


```sql
SELECT
created_on,
grant_option,
granted_by_name,
granted_by_role_type,
grantee_name,
grantee_type,
privileges,
securable_name,
securable_type
FROM snowflake.grant.grants_to
WHERE granteeName = '{{ granteeName }}'
AND granteeType = '{{ granteeType }}'
AND endpoint = '{{ endpoint }}';
```