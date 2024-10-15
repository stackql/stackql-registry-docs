---
title: live_pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - live_pipelines
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

Creates, updates, deletes, gets or lists a <code>live_pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.live_pipelines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_live_pipelines', value: 'view', },
        { label: 'live_pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="bitrate_kbps" /> | `text` | field from the `properties` object |
| <CopyableCode code="livePipelineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="topology_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Live pipeline properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, livePipelineName, resourceGroupName, subscriptionId" /> | Retrieves a specific live pipeline by name. If a live pipeline with that name has been previously created, the call will return the JSON representation of that instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves a list of live pipelines that have been created, along with their JSON representations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, livePipelineName, resourceGroupName, subscriptionId" /> | Creates a new live pipeline or updates an existing one, with the given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, livePipelineName, resourceGroupName, subscriptionId" /> | Deletes a live pipeline with the given name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, livePipelineName, resourceGroupName, subscriptionId" /> | Updates an existing live pipeline with the given name. Properties that can be updated include: description, bitrateKbps, and parameter definitions. Only the description can be updated while the live pipeline is active. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="accountName, livePipelineName, resourceGroupName, subscriptionId" /> | Activates a live pipeline with the given name. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="accountName, livePipelineName, resourceGroupName, subscriptionId" /> | Deactivates a live pipeline with the given name. |

## `SELECT` examples

Retrieves a list of live pipelines that have been created, along with their JSON representations.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_live_pipelines', value: 'view', },
        { label: 'live_pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
bitrate_kbps,
livePipelineName,
parameters,
resourceGroupName,
state,
subscriptionId,
topology_name
FROM azure.video_analyzer.vw_live_pipelines
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.video_analyzer.live_pipelines
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>live_pipelines</code> resource.

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
INSERT INTO azure.video_analyzer.live_pipelines (
accountName,
livePipelineName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ livePipelineName }}',
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
        - name: bitrateKbps
          value: integer
        - name: state
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

Updates a <code>live_pipelines</code> resource.

```sql
/*+ update */
UPDATE azure.video_analyzer.live_pipelines
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND livePipelineName = '{{ livePipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>live_pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.video_analyzer.live_pipelines
WHERE accountName = '{{ accountName }}'
AND livePipelineName = '{{ livePipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
