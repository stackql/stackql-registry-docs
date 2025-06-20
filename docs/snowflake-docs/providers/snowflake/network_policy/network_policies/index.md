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
| Name | Accessible by | Required Params | Optional Params | Description |
|:-----|:--------------|:----------------|:----------------|:------------|
| <CopyableCode code="fetch_network_policy" /> | `SELECT` | <CopyableCode code="name, endpoint" /> | - | Fetch a network policy |
| <CopyableCode code="list_network_policies" /> | `SELECT` | <CopyableCode code="endpoint" /> | - | List network policies |
| <CopyableCode code="create_network_policy" /> | `INSERT` | <CopyableCode code="data__name, endpoint" /> | <CopyableCode code="createMode" /> | Create a network policy |
| <CopyableCode code="delete_network_policy" /> | `DELETE` | <CopyableCode code="name, endpoint" /> | <CopyableCode code="ifExists" /> | Delete a network policy |

<br />


<details>
<summary>Optional Parameter Details</summary>

| Name | Description | Type | Default |
|------|-------------|------|---------|
| <CopyableCode code="createMode" /> | Query parameter allowing support for different modes of resource creation. Possible values include: - `errorIfExists`: Throws an error if you try to create a resource that already exists. - `orReplace`: Automatically replaces the existing resource with the current one. - `ifNotExists`: Creates a new resource when an alter is requested for a non-existent resource. | `string` | `errorIfExists` |
| <CopyableCode code="ifExists" /> | Query parameter that specifies how to handle the request for a resource that does not exist: - `true`: The endpoint does not throw an error if the resource does not exist. It returns a 200 success response, but does not take any action on the resource. - `false`: The endpoint throws an error if the resource doesn't exist. | `boolean` | `false` |

</details>

## `SELECT` examples

<Tabs
    defaultValue="list_network_policies"
    values={[
        { label: 'list_network_policies', value: 'list_network_policies' },
        { label: 'fetch_network_policy', value: 'fetch_network_policy' }
    ]
}>
<TabItem value="list_network_policies">

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
</TabItem>
<TabItem value="fetch_network_policy">

Fetch a network policy

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
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
</TabItem>
</Tabs>

## `INSERT` example

Create a network policy

<Tabs
    defaultValue="all"
    values={[
        { label: 'Required Properties', value: 'required' },
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO snowflake.network_policy.network_policies (
data__name,
data__allowed_network_rule_list,
data__blocked_network_rule_list,
data__allowed_ip_list,
data__blocked_ip_list,
data__comment,
endpoint
)
SELECT 
'{{ name }}',
'{{ allowed_network_rule_list }}',
'{{ blocked_network_rule_list }}',
'{{ allowed_ip_list }}',
'{{ blocked_ip_list }}',
'{{ comment }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="required">

```sql
/*+ create */
INSERT INTO snowflake.network_policy.network_policies (
data__name,
endpoint
)
SELECT 
'{{ name }}',
'{{ endpoint }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
# Description fields below are for documentation purposes only and are not required in the manifest
- name: network_policies
  props:
    - name: endpoint
      value: string
      description: Required parameter for the network_policies resource.
    - name: name
      value: string
      description: >-
        Name of the network policy (Required parameter for the network_policies
        resource.)
    - name: allowed_network_rule_list
      value: array
      description: List of names of allowed network rules in a network policy
    - name: blocked_network_rule_list
      value: array
      description: List of names of blocked network rules in a network policy
    - name: allowed_ip_list
      value: array
      description: List of allowed IPs in a network policy
    - name: blocked_ip_list
      value: array
      description: List of blocked IPs in a network policy
    - name: comment
      value: string
      description: user comment associated to an object in the dictionary
```
</TabItem>
</Tabs>

## `DELETE` example

Delete a network policy

```sql
/*+ delete */
DELETE FROM snowflake.network_policy.network_policies
WHERE name = '{{ name }}'
AND endpoint = '{{ endpoint }}';
```
