---
title: dns_records
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_records
  - networking
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

Creates, updates, deletes, gets or lists a <code>dns_records</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dns_records</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.networking.dns_records" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | The desired state of the Dns Record |
| <CopyableCode code="status" /> | `object` | The status of the Dns Record |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_networking_v1dns_record" /> | `SELECT` | <CopyableCode code="environment, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a DNS record. |
| <CopyableCode code="list_networking_v1dns_records" /> | `SELECT` | <CopyableCode code="environment" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all DNS records. |
| <CopyableCode code="create_networking_v1dns_record" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create a DNS record. |
| <CopyableCode code="delete_networking_v1dns_record" /> | `DELETE` | <CopyableCode code="environment, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a DNS record. |
| <CopyableCode code="update_networking_v1dns_record" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update a DNS record. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all DNS records.


```sql
SELECT
id,
_spec,
api_version,
kind,
metadata,
spec,
status
FROM confluent.networking.dns_records
WHERE environment = '{{ environment }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dns_records</code> resource.

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
INSERT INTO confluent.networking.dns_records (
data__spec
)
SELECT 
'{{ spec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: dns_records
  props:
    - name: spec
      props:
        - name: environment
          value: string
        - name: gateway
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dns_records</code> resource.

```sql
/*+ update */
UPDATE confluent.networking.dns_records
SET 
spec = '{{ spec }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>dns_records</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.networking.dns_records
WHERE environment = '{{ environment }}'
AND id = '{{ id }}';
```
