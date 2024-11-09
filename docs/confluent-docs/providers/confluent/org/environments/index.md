---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
  - org
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

Creates, updates, deletes, gets or lists a <code>environments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.org.environments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environments', value: 'view', },
        { label: 'environments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `text` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | A human-readable name for the Environment |
| <CopyableCode code="kind" /> | `text` | Kind defines the object this REST resource represents. |
| <CopyableCode code="resource_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="self" /> | `text` | field from the `properties` object |
| <CopyableCode code="stream_governance_package" /> | `text` | field from the `properties` object |
| <CopyableCode code="updated_at" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID is the "natural identifier" for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted ("time"); however, it may collide with IDs for other object `kinds` or objects of the same `kind` within a different scope/namespace ("space"). |
| <CopyableCode code="api_version" /> | `string` | APIVersion defines the schema version of this representation of a resource. |
| <CopyableCode code="display_name" /> | `string` | A human-readable name for the Environment |
| <CopyableCode code="kind" /> | `string` | Kind defines the object this REST resource represents. |
| <CopyableCode code="metadata" /> | `` | ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. |
| <CopyableCode code="stream_governance_config" /> | `object` | Stream Governance configurations for the environment |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_org_v2environment" /> | `SELECT` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to read an environment. |
| <CopyableCode code="list_org_v2environments" /> | `SELECT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all environments. |
| <CopyableCode code="create_org_v2environment" /> | `INSERT` | <CopyableCode code="" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to create an environment. |
| <CopyableCode code="delete_org_v2environment" /> | `DELETE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to delete an environment.

If successful, this request will also recursively delete all of the environment's associated resources,
including all Kafka clusters, connectors, etc. |
| <CopyableCode code="update_org_v2environment" /> | `UPDATE` | <CopyableCode code="id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Make a request to update an environment. |

## `SELECT` examples

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Retrieve a sorted, filtered, paginated list of all environments.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environments', value: 'view', },
        { label: 'environments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
api_version,
created_at,
display_name,
kind,
resource_name,
self,
stream_governance_package,
updated_at
FROM confluent.org.vw_environments
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
api_version,
display_name,
kind,
metadata,
stream_governance_config
FROM confluent.org.environments
;
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environments</code> resource.

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
INSERT INTO confluent.org.environments (
data__display_name
)
SELECT 
'{{ display_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: environments
  props:
    - name: display_name
      value: string
    - name: stream_governance_config
      props:
        - name: package
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>environments</code> resource.

```sql
/*+ update */
UPDATE confluent.org.environments
SET 
metadata = '{{ metadata }}',
display_name = '{{ display_name }}',
stream_governance_config = '{{ stream_governance_config }}'
WHERE 
id = '{{ id }}';
```

## `DELETE` example

Deletes the specified <code>environments</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.org.environments
WHERE id = '{{ id }}';
```
