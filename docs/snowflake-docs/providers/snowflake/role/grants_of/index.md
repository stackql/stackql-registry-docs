---
title: grants_of
hide_title: false
hide_table_of_contents: false
keywords:
  - grants_of
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

Creates, updates, deletes, gets or lists a <code>grants_of</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants_of</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.role.grants_of" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="created_on" /> | `string` | Date and time when the grant was created |
| <CopyableCode code="granted_by" /> | `string` | The role that granted this role to this grantee |
| <CopyableCode code="granted_to" /> | `string` | The type of the grantee, can be USER or ROLE |
| <CopyableCode code="grantee_name" /> | `string` | The name of the grantee |
| <CopyableCode code="role" /> | `string` | The name of the role |

## Methods
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="list_grants_of" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="showLimit" /> | List all grants of the role |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="showLimit" /> | Query parameter to limit the maximum number of rows returned by a command. | `integer` | `-` |

</details>

## `SELECT` examples

List all grants of the role


```sql
SELECT
created_on,
granted_by,
granted_to,
grantee_name,
role
FROM snowflake.role.grants_of
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```