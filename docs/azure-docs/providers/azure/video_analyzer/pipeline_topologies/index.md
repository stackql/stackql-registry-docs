---
title: pipeline_topologies
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_topologies
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

Creates, updates, deletes, gets or lists a <code>pipeline_topologies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_topologies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.pipeline_topologies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipeline_topologies', value: 'view', },
        { label: 'pipeline_topologies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | Topology kind. |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="pipelineTopologyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="processors" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sinks" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | The SKU details. |
| <CopyableCode code="sources" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Topology kind. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a pipeline topology. |
| <CopyableCode code="sku" /> | `object` | The SKU details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId" /> | Retrieves a specific pipeline topology by name. If a topology with that name has been previously created, the call will return the JSON representation of that topology. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Retrieves a list of pipeline topologies that have been added to the account, if any, along with their JSON representation. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId, data__kind, data__sku" /> | Creates a new pipeline topology or updates an existing one, with the given name. A pipeline topology describes the processing steps to be applied when processing content for a particular outcome. The topology should be defined according to the scenario to be achieved and can be reused across many pipeline instances which share the same processing characteristics. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId" /> | Deletes a pipeline topology with the given name. This method should be called after all instances of the topology have been stopped and deleted. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, pipelineTopologyName, resourceGroupName, subscriptionId" /> | Updates an existing pipeline topology with the given name. If the associated live pipelines or pipeline jobs are in active or processing state, respectively, then only the description can be updated. Else, the properties that can be updated include: description, parameter declarations, sources, processors, and sinks. |

## `SELECT` examples

Retrieves a list of pipeline topologies that have been added to the account, if any, along with their JSON representation.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipeline_topologies', value: 'view', },
        { label: 'pipeline_topologies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
accountName,
kind,
parameters,
pipelineTopologyName,
processors,
resourceGroupName,
sinks,
sku,
sources,
subscriptionId
FROM azure.video_analyzer.vw_pipeline_topologies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
properties,
sku
FROM azure.video_analyzer.pipeline_topologies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipeline_topologies</code> resource.

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
INSERT INTO azure.video_analyzer.pipeline_topologies (
accountName,
pipelineTopologyName,
resourceGroupName,
subscriptionId,
data__kind,
data__sku,
properties,
kind,
sku
)
SELECT 
'{{ accountName }}',
'{{ pipelineTopologyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__kind }}',
'{{ data__sku }}',
'{{ properties }}',
'{{ kind }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: description
          value: string
        - name: parameters
          value:
            - - name: name
                value: string
              - name: type
                value: string
              - name: description
                value: string
              - name: default
                value: string
        - name: sources
          value:
            - - name: '@type'
                value: string
              - name: name
                value: string
        - name: processors
          value:
            - - name: '@type'
                value: string
              - name: name
                value: string
              - name: inputs
                value:
                  - - name: nodeName
                      value: string
        - name: sinks
          value:
            - - name: '@type'
                value: string
              - name: name
                value: string
              - name: inputs
                value:
                  - - name: nodeName
                      value: string
    - name: kind
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pipeline_topologies</code> resource.

```sql
/*+ update */
UPDATE azure.video_analyzer.pipeline_topologies
SET 
properties = '{{ properties }}',
kind = '{{ kind }}',
sku = '{{ sku }}'
WHERE 
accountName = '{{ accountName }}'
AND pipelineTopologyName = '{{ pipelineTopologyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pipeline_topologies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.video_analyzer.pipeline_topologies
WHERE accountName = '{{ accountName }}'
AND pipelineTopologyName = '{{ pipelineTopologyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
