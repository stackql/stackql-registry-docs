---
title: pipeline_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_jobs
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>pipeline_jobs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.pipeline_jobs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipeline_jobs', value: 'view', },
        { label: 'pipeline_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="error" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="pipelineJobName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="topology_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Pipeline job properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Retrieves a specific pipeline job by name. If a pipeline job with that name has been previously created, the call will return the JSON representation of that instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves a list of all live pipelines that have been created, along with their JSON representations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Creates a new pipeline job or updates an existing one, with the given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Deletes a pipeline job with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Updates an existing pipeline job with the given name. Properties that can be updated include: description. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="accountName, pipelineJobName, resourceGroupName, subscriptionId" /> | Cancels a pipeline job with the given name. |

## `SELECT` examples

Retrieves a list of all live pipelines that have been created, along with their JSON representations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipeline_jobs', value: 'view', },
        { label: 'pipeline_jobs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
error,
expiration,
parameters,
pipelineJobName,
resourceGroupName,
state,
subscriptionId,
topology_name
FROM azure.video_analyzer.vw_pipeline_jobs
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.video_analyzer.pipeline_jobs
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipeline_jobs</code> resource.

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
INSERT INTO azure.video_analyzer.pipeline_jobs (
accountName,
pipelineJobName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ pipelineJobName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: topologyName
          value: string
        - name: description
          value: string
        - name: state
          value: string
        - name: expiration
          value: string
        - name: error
          value:
            - name: code
              value: string
            - name: message
              value: string
        - name: parameters
          value:
            - - name: name
                value: string
              - name: value
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pipeline_jobs</code> resource.

```sql
/*+ update */
UPDATE azure.video_analyzer.pipeline_jobs
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND pipelineJobName = '{{ pipelineJobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pipeline_jobs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.video_analyzer.pipeline_jobs
WHERE accountName = '{{ accountName }}'
AND pipelineJobName = '{{ pipelineJobName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
