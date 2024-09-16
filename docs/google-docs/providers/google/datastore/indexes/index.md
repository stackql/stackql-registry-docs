---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
  - datastore
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.datastore.indexes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ancestor" /> | `string` | Required. The index's ancestor mode. Must not be ANCESTOR_MODE_UNSPECIFIED. |
| <CopyableCode code="indexId" /> | `string` | Output only. The resource ID of the index. |
| <CopyableCode code="kind" /> | `string` | Required. The entity kind to which this index applies. |
| <CopyableCode code="projectId" /> | `string` | Output only. Project ID. |
| <CopyableCode code="properties" /> | `array` | Required. An ordered sequence of property names and their index attributes. Requires: * A maximum of 100 properties. |
| <CopyableCode code="state" /> | `string` | Output only. The state of the index. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="indexId, projectId" /> | Gets an index. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectId" /> | Lists the indexes that match the specified filters. Datastore uses an eventually consistent query to fetch the list of indexes and may occasionally return stale results. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectId" /> | Creates the specified index. A newly created index's initial state is `CREATING`. On completion of the returned google.longrunning.Operation, the state will be `READY`. If the index already exists, the call will return an `ALREADY_EXISTS` status. During index creation, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, removing the index with delete, then re-creating the index with create. Indexes with a single property cannot be created. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="indexId, projectId" /> | Deletes an existing index. An index can only be deleted if it is in a `READY` or `ERROR` state. On successful execution of the request, the index will be in a `DELETING` state. And on completion of the returned google.longrunning.Operation, the index will be removed. During index deletion, the process could result in an error, in which case the index will move to the `ERROR` state. The process can be recovered by fixing the data that caused the error, followed by calling delete again. |

## `SELECT` examples

Lists the indexes that match the specified filters. Datastore uses an eventually consistent query to fetch the list of indexes and may occasionally return stale results.

```sql
SELECT
ancestor,
indexId,
kind,
projectId,
properties,
state
FROM google.datastore.indexes
WHERE projectId = '{{ projectId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>indexes</code> resource.

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
INSERT INTO google.datastore.indexes (
projectId,
ancestor,
properties
)
SELECT 
'{{ projectId }}',
'{{ ancestor }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: ancestor
      value: '{{ ancestor }}'
    - name: properties
      value:
        - name: $ref
          value: '{{ $ref }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>indexes</code> resource.

```sql
/*+ delete */
DELETE FROM google.datastore.indexes
WHERE indexId = '{{ indexId }}'
AND projectId = '{{ projectId }}';
```
