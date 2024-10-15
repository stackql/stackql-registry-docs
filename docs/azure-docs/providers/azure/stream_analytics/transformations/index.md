---
title: transformations
hide_title: false
hide_table_of_contents: false
keywords:
  - transformations
  - stream_analytics
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

Creates, updates, deletes, gets or lists a <code>transformations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transformations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.transformations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_transformations', value: 'view', },
        { label: 'transformations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="query" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="streaming_units" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="transformationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="valid_streaming_units" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with a transformation. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, transformationName" /> | Gets details about the specified transformation. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, transformationName" /> | Creates a transformation or replaces an already existing transformation under an existing streaming job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobName, resourceGroupName, subscriptionId, transformationName" /> | Updates an existing transformation under an existing streaming job. This can be used to partially update (ie. update one or two properties) a transformation without affecting the rest the job or transformation definition. |

## `SELECT` examples

Gets details about the specified transformation.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_transformations', value: 'view', },
        { label: 'transformations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
jobName,
query,
resourceGroupName,
streaming_units,
subscriptionId,
transformationName,
type,
valid_streaming_units
FROM azure.stream_analytics.vw_transformations
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND transformationName = '{{ transformationName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.stream_analytics.transformations
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND transformationName = '{{ transformationName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transformations</code> resource.

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
INSERT INTO azure.stream_analytics.transformations (
jobName,
resourceGroupName,
subscriptionId,
transformationName,
name,
properties
)
SELECT 
'{{ jobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ transformationName }}',
'{{ name }}',
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
    - name: type
      value: string
    - name: properties
      value:
        - name: streamingUnits
          value: integer
        - name: validStreamingUnits
          value:
            - integer
        - name: query
          value: string
        - name: etag
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>transformations</code> resource.

```sql
/*+ update */
UPDATE azure.stream_analytics.transformations
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND transformationName = '{{ transformationName }}';
```
