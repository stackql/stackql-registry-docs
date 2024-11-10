---
title: api_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - api_keys
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

Creates, updates, deletes, gets or lists a <code>api_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>api_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.iam.api_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | The desired state of the Api Key |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_iam_v2api_key" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read an API key. |
| <CopyableCode code="list_iam_v2api_keys" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all API keys. This can show all keys for a single owner (across resources - Kafka clusters), or all keys for a single resource (across owners). If no `owner` or `resource` filters are specified, returns all API Keys in the organization. You will only see the keys that are accessible to the account making the API request. |
| <CopyableCode code="create_iam_v2api_key" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create an API key. |
| <CopyableCode code="delete_iam_v2api_key" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete an API key. |
| <CopyableCode code="update_iam_v2api_key" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update an API key. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all API keys. This can show all keys for a single owner (across resources - Kafka clusters), or all keys for a single resource (across owners). If no `owner` or `resource` filters are specified, returns all API Keys in the organization. You will only see the keys that are accessible to the account making the API request.


```sql
SELECT
id,
_spec,
api_version,
kind,
metadata,
spec
FROM confluent.iam.api_keys
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>api_keys</code> resource.

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
INSERT INTO confluent.iam.api_keys (
data__spec
)
SELECT 
'{{ spec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: api_keys
  props:
    - name: spec
      props:
        - name: owner
          value: string
        - name: resource
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>api_keys</code> resource.

```sql
/*+ update */
UPDATE confluent.iam.api_keys
SET 

WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>api_keys</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.iam.api_keys
WHERE id = '{{ id }}';
```
