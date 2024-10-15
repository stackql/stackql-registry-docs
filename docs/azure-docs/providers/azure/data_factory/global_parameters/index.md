---
title: global_parameters
hide_title: false
hide_table_of_contents: false
keywords:
  - global_parameters
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>global_parameters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_parameters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.global_parameters" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_global_parameters', value: 'view', },
        { label: 'global_parameters', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="globalParameterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | Global parameters associated with the Azure Data Factory |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, globalParameterName, resourceGroupName, subscriptionId" /> | Gets a Global parameter |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Lists Global parameters |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="factoryName, globalParameterName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a Global parameter |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factoryName, globalParameterName, resourceGroupName, subscriptionId" /> | Deletes a Global parameter |

## `SELECT` examples

Lists Global parameters

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_global_parameters', value: 'view', },
        { label: 'global_parameters', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
factoryName,
globalParameterName,
resourceGroupName,
subscriptionId,
type
FROM azure.data_factory.vw_global_parameters
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.data_factory.global_parameters
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>global_parameters</code> resource.

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
INSERT INTO azure.data_factory.global_parameters (
factoryName,
globalParameterName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ factoryName }}',
'{{ globalParameterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: etag
      value: string
    - name: properties
      value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>global_parameters</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.global_parameters
WHERE factoryName = '{{ factoryName }}'
AND globalParameterName = '{{ globalParameterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
