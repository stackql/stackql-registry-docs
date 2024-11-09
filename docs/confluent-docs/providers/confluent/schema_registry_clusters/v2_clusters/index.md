---
title: v2_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - v2_clusters
  - schema_registry_clusters
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

Creates, updates, deletes, gets or lists a <code>v2_clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>v2_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry_clusters.v2_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | The desired state of the Cluster |
| <CopyableCode code="status" /> | `object` | The status of the Cluster |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_srcm_v2cluster" /> | `SELECT` | <CopyableCode code="environment, id" /> | [![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy)

Make a request to read a cluster. |
| <CopyableCode code="list_srcm_v2clusters" /> | `SELECT` | <CopyableCode code="environment" /> | [![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all clusters. |
| <CopyableCode code="create_srcm_v2cluster" /> | `INSERT` | <CopyableCode code="" /> | [![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy)

Make a request to create a cluster. |
| <CopyableCode code="delete_srcm_v2cluster" /> | `DELETE` | <CopyableCode code="environment, id" /> | [![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy)

Make a request to delete a cluster. |
| <CopyableCode code="update_srcm_v2cluster" /> | `UPDATE` | <CopyableCode code="id" /> | [![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy)

Make a request to update a cluster. |

## `SELECT` examples

[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all clusters.


```sql
SELECT
id,
_spec,
api_version,
kind,
metadata,
spec,
status
FROM confluent.schema_registry_clusters.v2_clusters
WHERE environment = '{{ environment }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>v2_clusters</code> resource.

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
INSERT INTO confluent.schema_registry_clusters.v2_clusters (
data__spec
)
SELECT 
'{{ spec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: v2_clusters
  props:
    - name: spec
      props:
        - name: environment
          value: string
        - name: region
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>v2_clusters</code> resource.

```sql
/*+ update */
UPDATE confluent.schema_registry_clusters.v2_clusters
SET 

WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>v2_clusters</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.schema_registry_clusters.v2_clusters
WHERE environment = '{{ environment }}'
AND id = '{{ id }}';
```
