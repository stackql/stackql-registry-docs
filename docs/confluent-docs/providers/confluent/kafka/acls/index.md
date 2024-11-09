---
title: acls
hide_title: false
hide_table_of_contents: false
keywords:
  - acls
  - kafka
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>acls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.acls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="host" /> | `string` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="operation" /> | `string` |  |
| <CopyableCode code="pattern_type" /> | `string` |  |
| <CopyableCode code="permission" /> | `string` |  |
| <CopyableCode code="principal" /> | `string` |  |
| <CopyableCode code="resource_name" /> | `string` |  |
| <CopyableCode code="resource_type" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_acls" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return a list of ACLs that match the search criteria. |
| <CopyableCode code="create_kafka_acls" /> | `INSERT` | <CopyableCode code="cluster_id, data__host, data__operation, data__pattern_type, data__permission, data__principal, data__resource_name, data__resource_type" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Create an ACL. |
| <CopyableCode code="delete_kafka_acls" /> | `DELETE` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Delete the ACLs that match the search criteria. |
| <CopyableCode code="batch_create_kafka_acls" /> | `EXEC` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Create ACLs. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return a list of ACLs that match the search criteria.


```sql
SELECT
cluster_id,
host,
kind,
metadata,
operation,
pattern_type,
permission,
principal,
resource_name,
resource_type
FROM confluent.kafka.acls
WHERE cluster_id = '{{ cluster_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>acls</code> resource.

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
INSERT INTO confluent.kafka.acls (
data__resource_type,
data__resource_name,
data__pattern_type,
data__principal,
data__host,
data__operation,
data__permission,
cluster_id
)
SELECT 
'{{ resource_type }}',
'{{ resource_name }}',
'{{ pattern_type }}',
'{{ principal }}',
'{{ host }}',
'{{ operation }}',
'{{ permission }}',
'{{ cluster_id }}',
'{{ data__host }}',
'{{ data__operation }}',
'{{ data__pattern_type }}',
'{{ data__permission }}',
'{{ data__principal }}',
'{{ data__resource_name }}',
'{{ data__resource_type }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: acls
  props:
    - name: cluster_id
      value: string
    - name: data__host
      value: string
    - name: data__operation
      value: string
    - name: data__pattern_type
      value: string
    - name: data__permission
      value: string
    - name: data__principal
      value: string
    - name: data__resource_name
      value: string
    - name: data__resource_type
      value: string
    - name: resource_type
      value: string
    - name: resource_name
      value: string
    - name: pattern_type
      value: string
    - name: principal
      value: string
    - name: host
      value: string
    - name: operation
      value: string
    - name: permission
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>acls</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.kafka.acls
WHERE cluster_id = '{{ cluster_id }}';
```
