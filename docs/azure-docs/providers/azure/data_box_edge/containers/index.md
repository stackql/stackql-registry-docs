---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - data_box_edge
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

Creates, updates, deletes, gets or lists a <code>containers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box_edge.containers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_containers', value: 'view', },
        { label: 'containers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `text` | The object name. |
| <CopyableCode code="containerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="container_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_format" /> | `text` | field from the `properties` object |
| <CopyableCode code="deviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="refresh_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The hierarchical type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The path ID that uniquely identifies the object. |
| <CopyableCode code="name" /> | `string` | The object name. |
| <CopyableCode code="properties" /> | `object` | The container properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The hierarchical type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId" /> |  |
| <CopyableCode code="list_by_storage_account" /> | `SELECT` | <CopyableCode code="deviceName, resourceGroupName, storageAccountName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId" /> | Deletes the container on the Data Box Edge/Data Box Gateway device. |
| <CopyableCode code="refresh" /> | `EXEC` | <CopyableCode code="containerName, deviceName, resourceGroupName, storageAccountName, subscriptionId" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_containers', value: 'view', },
        { label: 'containers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
containerName,
container_status,
created_date_time,
data_format,
deviceName,
refresh_details,
resourceGroupName,
storageAccountName,
subscriptionId,
system_data,
type
FROM azure.data_box_edge.vw_containers
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageAccountName = '{{ storageAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_box_edge.containers
WHERE deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageAccountName = '{{ storageAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>containers</code> resource.

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
INSERT INTO azure.data_box_edge.containers (
containerName,
deviceName,
resourceGroupName,
storageAccountName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ containerName }}',
'{{ deviceName }}',
'{{ resourceGroupName }}',
'{{ storageAccountName }}',
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
    - name: properties
      value:
        - name: containerStatus
          value: string
        - name: dataFormat
          value: string
        - name: refreshDetails
          value:
            - name: inProgressRefreshJobId
              value: string
            - name: lastCompletedRefreshJobTimeInUTC
              value: string
            - name: errorManifestFile
              value: string
            - name: lastJob
              value: string
        - name: createdDateTime
          value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>containers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_box_edge.containers
WHERE containerName = '{{ containerName }}'
AND deviceName = '{{ deviceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageAccountName = '{{ storageAccountName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
