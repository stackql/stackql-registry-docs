---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - sql
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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.sql.connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The user provided name of the resource, unique within this environment. |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | Encapsulates the model provider access details |
| <CopyableCode code="status" /> | `object` | The status of the Connection |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_sqlv1connection" /> | `SELECT` | <CopyableCode code="connection_name, environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a Connection. |
| <CopyableCode code="list_sqlv1connections" /> | `SELECT` | <CopyableCode code="environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered and paginated list of all Connections. |
| <CopyableCode code="create_sqlv1connection" /> | `INSERT` | <CopyableCode code="environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) Make a request to create a Connection. |
| <CopyableCode code="delete_sqlv1connection" /> | `DELETE` | <CopyableCode code="connection_name, environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a statement. |
| <CopyableCode code="update_sqlv1connection" /> | `EXEC` | <CopyableCode code="connection_name, environment_id, organization_id" /> | [![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) Make a request to update a connection. |

## `SELECT` examples

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered and paginated list of all Connections.


```sql
SELECT
name,
_spec,
api_version,
kind,
metadata,
spec,
status
FROM confluent.sql.connections
WHERE environment_id = '{{ environment_id }}'
AND organization_id = '{{ organization_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

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
INSERT INTO confluent.sql.connections (
data__spec,
data__name,
environment_id,
organization_id
)
SELECT 
'{{ spec }}',
'{{ name }}',
'{{ environment_id }}',
'{{ organization_id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: connections
  props:
    - name: environment_id
      value: string
    - name: organization_id
      value: string
    - name: name
      value: string
    - name: spec
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>connections</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.sql.connections
WHERE connection_name = '{{ connection_name }}'
AND environment_id = '{{ environment_id }}'
AND organization_id = '{{ organization_id }}';
```
