---
title: graph_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - graph_queries
  - resource_graph
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

Creates, updates, deletes, gets or lists a <code>graph_queries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>graph_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_graph.graph_queries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_graph_queries', value: 'view', },
        { label: 'graph_queries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Azure resource Id |
| <CopyableCode code="name" /> | `text` | Azure resource name. This is GUID value. The display name should be assigned within properties field. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | This will be used to handle Optimistic Concurrency. If not present, it will always overwrite the existing resource without checking conflict. |
| <CopyableCode code="location" /> | `text` | The location of the resource |
| <CopyableCode code="query" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="result_kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="time_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Azure resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name. This is GUID value. The display name should be assigned within properties field. |
| <CopyableCode code="etag" /> | `string` | This will be used to handle Optimistic Concurrency. If not present, it will always overwrite the existing resource without checking conflict. |
| <CopyableCode code="location" /> | `string` | The location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties that contain a graph query. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Azure resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Get a single graph query by its resourceName. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all graph queries defined within a specified subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all graph queries defined within a specified subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Create a new graph query. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Delete a graph query. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates a graph query that has already been added. |

## `SELECT` examples

Get all graph queries defined within a specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_graph_queries', value: 'view', },
        { label: 'graph_queries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
etag,
location,
query,
resourceGroupName,
resourceName,
result_kind,
subscriptionId,
tags,
time_modified,
type
FROM azure.resource_graph.vw_graph_queries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.resource_graph.graph_queries
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>graph_queries</code> resource.

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
INSERT INTO azure.resource_graph.graph_queries (
resourceGroupName,
resourceName,
subscriptionId,
location,
etag,
tags,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ etag }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: location
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: tags
      value: object
    - name: properties
      value:
        - name: timeModified
          value: string
        - name: description
          value: string
        - name: query
          value: string
        - name: resultKind
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>graph_queries</code> resource.

```sql
/*+ update */
UPDATE azure.resource_graph.graph_queries
SET 
tags = '{{ tags }}',
etag = '{{ etag }}',
properties = '{{ properties }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>graph_queries</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resource_graph.graph_queries
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
