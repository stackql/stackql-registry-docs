---
title: grants_on
hide_title: false
hide_table_of_contents: false
keywords:
  - grants_on
  - role
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

Creates, updates, deletes, gets or lists a <code>grants_on</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants_on</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.role.grants_on" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the role |
| <CopyableCode code="created_on" /> | `string` | Date and time when the grant was created |
| <CopyableCode code="grant_option" /> | `string` | If true, allows the recipient role to grant the privileges to other roles. |
| <CopyableCode code="granted_by" /> | `string` | The role that granted this privilege to this grantee |
| <CopyableCode code="granted_by_role_type" /> | `string` | Type of the role that granted this privilege to this grantee |
| <CopyableCode code="granted_on" /> | `string` | The type of of the role |
| <CopyableCode code="granted_to" /> | `string` | The type of the grantee |
| <CopyableCode code="grantee_name" /> | `string` | The name of the grantee |
| <CopyableCode code="privilege" /> | `string` | The name of the privilege |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_grants_on" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="showLimit" /> | List all grants on the role |
<br />
Expand this to view optional parameter details for all methods in this resource.


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |

</details>

## `SELECT` examples

List all grants on the role


```sql
SELECT
name,
created_on,
grant_option,
granted_by,
granted_by_role_type,
granted_on,
granted_to,
grantee_name,
privilege
FROM snowflake.role.grants_on
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```