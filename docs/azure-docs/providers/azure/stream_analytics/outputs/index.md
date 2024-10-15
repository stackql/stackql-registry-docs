---
title: outputs
hide_title: false
hide_table_of_contents: false
keywords:
  - outputs
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

Creates, updates, deletes, gets or lists a <code>outputs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.stream_analytics.outputs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_outputs', value: 'view', },
        { label: 'outputs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="datasource" /> | `text` | field from the `properties` object |
| <CopyableCode code="diagnostics" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="jobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="outputName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serialization" /> | `text` | field from the `properties` object |
| <CopyableCode code="size_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | The properties that are associated with an output. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Gets details about the specified output. |
| <CopyableCode code="list_by_streaming_job" /> | `SELECT` | <CopyableCode code="jobName, resourceGroupName, subscriptionId" /> | Lists all of the outputs under the specified streaming job. |
| <CopyableCode code="create_or_replace" /> | `INSERT` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Creates an output or replaces an already existing output under an existing streaming job. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Deletes an output from the streaming job. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Updates an existing output under an existing streaming job. This can be used to partially update (ie. update one or two properties) an output without affecting the rest the job or output definition. |
| <CopyableCode code="test" /> | `EXEC` | <CopyableCode code="jobName, outputName, resourceGroupName, subscriptionId" /> | Tests whether an output’s datasource is reachable and usable by the Azure Stream Analytics service. |

## `SELECT` examples

Lists all of the outputs under the specified streaming job.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_outputs', value: 'view', },
        { label: 'outputs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
datasource,
diagnostics,
etag,
jobName,
outputName,
resourceGroupName,
serialization,
size_window,
subscriptionId,
time_window,
type
FROM azure.stream_analytics.vw_outputs
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.stream_analytics.outputs
WHERE jobName = '{{ jobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>outputs</code> resource.

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
INSERT INTO azure.stream_analytics.outputs (
jobName,
outputName,
resourceGroupName,
subscriptionId,
name,
properties
)
SELECT 
'{{ jobName }}',
'{{ outputName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
        - name: datasource
          value:
            - name: type
              value: string
        - name: timeWindow
          value: string
        - name: sizeWindow
          value: integer
        - name: serialization
          value:
            - name: type
              value: []
        - name: diagnostics
          value:
            - name: conditions
              value:
                - - name: since
                    value: string
                  - name: code
                    value: string
                  - name: message
                    value: string
        - name: etag
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>outputs</code> resource.

```sql
/*+ update */
UPDATE azure.stream_analytics.outputs
SET 
name = '{{ name }}',
properties = '{{ properties }}'
WHERE 
jobName = '{{ jobName }}'
AND outputName = '{{ outputName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>outputs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.stream_analytics.outputs
WHERE jobName = '{{ jobName }}'
AND outputName = '{{ outputName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
