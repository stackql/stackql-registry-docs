---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - managed_kafka_clusters
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.managed_kafka_clusters.clusters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_endpoint" /> | `text` | field from the parent object |
| <CopyableCode code="api_version" /> | `text` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="availability" /> | `text` | field from the parent object |
| <CopyableCode code="cloud" /> | `text` | field from the parent object |
| <CopyableCode code="config_kind" /> | `text` | field from the parent object |
| <CopyableCode code="created_at" /> | `text` | field from the parent object |
| <CopyableCode code="display_name" /> | `text` | field from the parent object |
| <CopyableCode code="environment" /> | `text` | field from the parent object |
| <CopyableCode code="environment_id" /> | `text` | field from the parent object |
| <CopyableCode code="environment_related" /> | `text` | field from the parent object |
| <CopyableCode code="environment_resource_name" /> | `text` | field from the parent object |
| <CopyableCode code="http_endpoint" /> | `text` | field from the parent object |
| <CopyableCode code="kafka_bootstrap_endpoint" /> | `text` | field from the parent object |
| <CopyableCode code="kind" /> | `text` | Kind defines the object this REST resource represents. |
| <CopyableCode code="region" /> | `text` | field from the parent object |
| <CopyableCode code="resource_name" /> | `text` | field from the parent object |
| <CopyableCode code="self" /> | `text` | field from the parent object |
| <CopyableCode code="status_phase" /> | `text` | field from the parent object |
| <CopyableCode code="updated_at" /> | `text` | field from the parent object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="_spec" /> | `object` |  |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="spec" /> | `object` | The desired state of the Cluster |
| <CopyableCode code="status" /> | `object` | The status of the Cluster |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_cmk_v2cluster" /> | `SELECT` | <CopyableCode code="environment, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to read a cluster. |
| <CopyableCode code="list_cmk_v2clusters" /> | `SELECT` | <CopyableCode code="environment" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all clusters. |
| <CopyableCode code="create_cmk_v2cluster" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to create a cluster. |
| <CopyableCode code="delete_cmk_v2cluster" /> | `DELETE` | <CopyableCode code="environment, id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to delete a cluster. |
| <CopyableCode code="update_cmk_v2cluster" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Make a request to update a cluster. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Retrieve a sorted, filtered, paginated list of all clusters.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_clusters', value: 'view', },
        { label: 'clusters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
api_endpoint,
api_version,
availability,
cloud,
config_kind,
created_at,
display_name,
environment,
environment_id,
environment_related,
environment_resource_name,
http_endpoint,
kafka_bootstrap_endpoint,
kind,
region,
resource_name,
self,
status_phase,
updated_at
FROM confluent.managed_kafka_clusters.vw_clusters
WHERE environment = '{{ environment }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
_spec,
api_version,
kind,
metadata,
spec,
status
FROM confluent.managed_kafka_clusters.clusters
WHERE environment = '{{ environment }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>clusters</code> resource.

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
INSERT INTO confluent.managed_kafka_clusters.clusters (
data__spec
)
SELECT 
'{{ spec }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: clusters
  props:
    - name: spec
      props:
        - name: display_name
          value: string
        - name: availability
          value: string
        - name: cloud
          value: string
        - name: region
          value: string
        - name: config
          props:
            - name: kind
              value: string
        - name: environment
          props:
            - name: id
              value: string
            - name: environment
              value: string
        - name: network
          props:
            - name: id
              value: string
            - name: environment
              value: string
        - name: byok
          props:
            - name: id
              value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>clusters</code> resource.

```sql
/*+ update */
UPDATE confluent.managed_kafka_clusters.clusters
SET 
spec = '{{ spec }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>clusters</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.managed_kafka_clusters.clusters
WHERE environment = '{{ environment }}'
AND id = '{{ id }}';
```
