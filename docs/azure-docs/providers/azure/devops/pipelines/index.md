---
title: pipelines
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines
  - devops
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.devops.pipelines" /></td></tr>
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
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="bootstrap_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="organization" /> | `text` | field from the `properties` object |
| <CopyableCode code="pipelineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="pipeline_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="project" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource Tags |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Custom properties of a Pipeline. |
| <CopyableCode code="tags" /> | `object` | Resource Tags |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Gets an existing Azure Pipeline. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Azure Pipelines under the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Azure Pipelines under the specified subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates an Azure Pipeline. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Deletes an Azure Pipeline. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="pipelineName, resourceGroupName, subscriptionId" /> | Updates the properties of an Azure Pipeline. Currently, only tags can be updated. |

## `SELECT` examples

Lists all Azure Pipelines under the specified subscription.

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
id,
name,
bootstrap_configuration,
location,
organization,
pipelineName,
pipeline_id,
project,
resourceGroupName,
subscriptionId,
tags,
type
FROM azure.devops.vw_pipelines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.devops.pipelines
WHERE subscriptionId = '{{ subscriptionId }}';
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
INSERT INTO azure.devops.pipelines (
pipelineName,
resourceGroupName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ pipelineName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
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
        - name: pipelineId
          value: integer
        - name: organization
          value:
            - name: id
              value: string
            - name: name
              value: string
        - name: project
          value:
            - name: id
              value: string
            - name: name
              value: string
        - name: bootstrapConfiguration
          value:
            - name: repository
              value:
                - name: repositoryType
                  value: string
                - name: id
                  value: string
                - name: defaultBranch
                  value: string
                - name: authorization
                  value:
                    - name: authorizationType
                      value: string
                    - name: parameters
                      value: object
                - name: properties
                  value: object
            - name: template
              value:
                - name: id
                  value: string
                - name: parameters
                  value: object
    - name: id
      value: string
    - name: type
      value: string
    - name: tags
      value: object
    - name: location
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>pipelines</code> resource.

```sql
/*+ update */
UPDATE azure.devops.pipelines
SET 
tags = '{{ tags }}'
WHERE 
pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>pipelines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.devops.pipelines
WHERE pipelineName = '{{ pipelineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
