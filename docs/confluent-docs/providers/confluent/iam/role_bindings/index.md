---
title: role_bindings
hide_title: false
hide_table_of_contents: false
keywords:
  - role_bindings
  - iam
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>role_bindings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_bindings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.role_bindings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="crn_pattern" /> | `string` | A CRN that specifies the scope and resource patterns necessary for the role to bind |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="principal" /> | `string` | The principal User to bind the role to |
| <CopyableCode code="role_name" /> | `string` | The name of the role to bind to the principal |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2role_binding" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a role binding. |
| <CopyableCode code="list_iam_v2role_bindings" /> | `SELECT` | <CopyableCode code="crn_pattern" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all role bindings. |
| <CopyableCode code="create_iam_v2role_binding" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create a role binding. |
| <CopyableCode code="delete_iam_v2role_binding" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a role binding. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a role binding.


```sql
SELECT
id,
api_version,
crn_pattern,
kind,
metadata,
principal,
role_name
FROM confluent.iam.role_bindings
WHERE id = '{{ id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>role_bindings</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO confluent.iam.role_bindings (
data__principal,
data__role_name,
data__crn_pattern
)
SELECT 
'{{ principal }}',
'{{ role_name }}',
'{{ crn_pattern }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: role_bindings
  props:
    - name: principal
      value: string
    - name: role_name
      value: string
    - name: crn_pattern
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>role_bindings</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.role_bindings
WHERE id = '{{ id }}';
```
