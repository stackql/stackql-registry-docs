---
title: network_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - network_policies
  - network_policy
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

Creates, updates, deletes, gets or lists a <code>network_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="snowflake.network_policy.network_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the network policy |
| <CopyableCode code="allowed_ip_list" /> | `array` | List of allowed IPs in a network policy |
| <CopyableCode code="allowed_network_rule_list" /> | `array` | List of names of allowed network rules in a network policy |
| <CopyableCode code="blocked_ip_list" /> | `array` | List of blocked IPs in a network policy |
| <CopyableCode code="blocked_network_rule_list" /> | `array` | List of names of blocked network rules in a network policy |
| <CopyableCode code="comment" /> | `string` | user comment associated to an object in the dictionary |
| <CopyableCode code="created_on" /> | `string` | Date and time when the network policy was created. |
| <CopyableCode code="owner" /> | `string` | Role that owns the network policy |
| <CopyableCode code="owner_role_type" /> | `string` | The type of role that owns the network policy |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="fetch_network_policy" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | Fetch a network policy |
| <CopyableCode code="list_network_policies" /> | `SELECT` | <CopyableCode code="endpoint" /> | List network policies |
| <CopyableCode code="create_network_policy" /> | `INSERT` | <CopyableCode code="data__name, endpoint" /> | Create a network policy |
| <CopyableCode code="delete_network_policy" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | Delete a network policy |

## `SELECT` examples

List network policies


```sql
SELECT
name,
allowed_ip_list,
allowed_network_rule_list,
blocked_ip_list,
blocked_network_rule_list,
comment,
created_on,
owner,
owner_role_type
FROM snowflake.network_policy.network_policies
WHERE endpoint = '{{ endpoint }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>network_policies</code> resource.

<Tabs     defaultValue="all"    values={[        { label: 'All Properties', value: 'all' }, { label: 'Manifest', value: 'manifest' }    ]}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.network_policy.network_policies (
endpoint,
data__name
)
SELECT 
'{ name }',
'{ endpoint }'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: network_policies
  props:
  - name: data__name
    value: string
  - name: endpoint
    value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>network_policies</code> resource.

```sql
/*+ delete */
DELETE FROM snowflake.network_policy.network_policies
WHERE name = '{ name }' AND endpoint = '{ endpoint }';
```
