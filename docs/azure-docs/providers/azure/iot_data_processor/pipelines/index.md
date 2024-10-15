---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - iot_data_processor
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

Creates, updates, deletes, gets or lists a <code>pipelines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_data_processor.pipelines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipelines', value: 'view', },
        { label: 'pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="input" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="pipelineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="stages" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Pipeline resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceName, pipelineName, resourceGroupName, subscriptionId" /> | Get a Pipeline |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceName, pipelineName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a Pipeline |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceName, pipelineName, resourceGroupName, subscriptionId" /> | Delete a Pipeline |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="instanceName, pipelineName, resourceGroupName, subscriptionId" /> | Update a Pipeline |

## `SELECT` examples

Get a Pipeline

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_pipelines', value: 'view', },
        { label: 'pipelines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
enabled,
extended_location,
input,
instanceName,
location,
pipelineName,
provisioning_state,
resourceGroupName,
stages,
subscriptionId,
tags
FROM azure.iot_data_processor.vw_pipelines
WHERE instanceName = '{{ instanceName }}'
AND pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.iot_data_processor.pipelines
WHERE instanceName = '{{ instanceName }}'
AND pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pipelines</code> resource.

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
INSERT INTO azure.iot_data_processor.pipelines (
instanceName,
pipelineName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ instanceName }}',
'{{ pipelineName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
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
        - name: enabled
          value: boolean
        - name: input
          value:
            - name: type
              value: string
            - name: description
              value: string
            - name: next
              value:
                - string
        - name: stages
          value: object
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pipelines</code> resource.

```sql
/*+ update */
UPDATE azure.iot_data_processor.pipelines
SET 
tags = '{{ tags }}'
WHERE 
instanceName = '{{ instanceName }}'
AND pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_data_processor.pipelines
WHERE instanceName = '{{ instanceName }}'
AND pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
