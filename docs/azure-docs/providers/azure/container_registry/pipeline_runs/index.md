---
title: pipeline_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_runs
  - container_registry
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

Creates, updates, deletes, gets or lists a <code>pipeline_runs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_registry.pipeline_runs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipeline_runs', value: 'view', },
        { label: 'pipeline_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="force_update_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="pipelineRunName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="request" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="response" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of a pipeline run. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pipelineRunName, registryName, resourceGroupName, subscriptionId" /> | Gets the detailed information for a given pipeline run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="registryName, resourceGroupName, subscriptionId" /> | Lists all the pipeline runs for the specified container registry. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="pipelineRunName, registryName, resourceGroupName, subscriptionId" /> | Creates a pipeline run for a container registry with the specified parameters |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pipelineRunName, registryName, resourceGroupName, subscriptionId" /> | Deletes a pipeline run from a container registry. |

## `SELECT` examples

Lists all the pipeline runs for the specified container registry.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipeline_runs', value: 'view', },
        { label: 'pipeline_runs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
force_update_tag,
pipelineRunName,
provisioning_state,
registryName,
request,
resourceGroupName,
response,
subscriptionId
FROM azure.container_registry.vw_pipeline_runs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.container_registry.pipeline_runs
WHERE registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipeline_runs</code> resource.

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
INSERT INTO azure.container_registry.pipeline_runs (
pipelineRunName,
registryName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ pipelineRunName }}',
'{{ registryName }}',
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
        - name: provisioningState
          value: string
        - name: request
          value:
            - name: pipelineResourceId
              value: string
            - name: artifacts
              value:
                - string
            - name: source
              value:
                - name: type
                  value: string
                - name: name
                  value: string
            - name: target
              value:
                - name: type
                  value: string
                - name: name
                  value: string
            - name: catalogDigest
              value: string
        - name: response
          value:
            - name: status
              value: string
            - name: importedArtifacts
              value:
                - string
            - name: progress
              value:
                - name: percentage
                  value: string
            - name: startTime
              value: string
            - name: finishTime
              value: string
            - name: source
              value:
                - name: type
                  value: string
                - name: uri
                  value: string
                - name: keyVaultUri
                  value: string
            - name: target
              value:
                - name: type
                  value: string
                - name: uri
                  value: string
                - name: keyVaultUri
                  value: string
            - name: catalogDigest
              value: string
            - name: trigger
              value:
                - name: sourceTrigger
                  value:
                    - name: timestamp
                      value: string
            - name: pipelineRunErrorMessage
              value: string
        - name: forceUpdateTag
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>pipeline_runs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.container_registry.pipeline_runs
WHERE pipelineRunName = '{{ pipelineRunName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
