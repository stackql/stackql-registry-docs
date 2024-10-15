---
title: data_flows
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flows
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

Creates, updates, deletes, gets or lists a <code>data_flows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.data_flows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_flows', value: 'view', },
        { label: 'data_flows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotations" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataFlowName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="folder" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Azure Data Factory nested object which contains a flow with data movements and transformations. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataFlowName, factoryName, resourceGroupName, subscriptionId" /> | Gets a data flow. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Lists data flows. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataFlowName, factoryName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a data flow. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataFlowName, factoryName, resourceGroupName, subscriptionId" /> | Deletes a data flow. |

## `SELECT` examples

Lists data flows.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_flows', value: 'view', },
        { label: 'data_flows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
annotations,
dataFlowName,
etag,
factoryName,
folder,
resourceGroupName,
subscriptionId,
type
FROM azure.data_factory.vw_data_flows
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
FROM azure.data_factory.data_flows
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_flows</code> resource.

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
INSERT INTO azure.data_factory.data_flows (
dataFlowName,
factoryName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ dataFlowName }}',
'{{ factoryName }}',
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
      value:
        - name: type
          value: string
        - name: description
          value: string
        - name: annotations
          value:
            - object
        - name: folder
          value:
            - name: name
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_flows</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.data_flows
WHERE dataFlowName = '{{ dataFlowName }}'
AND factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
