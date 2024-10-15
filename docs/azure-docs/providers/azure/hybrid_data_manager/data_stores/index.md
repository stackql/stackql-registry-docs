---
title: data_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - data_stores
  - hybrid_data_manager
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

Creates, updates, deletes, gets or lists a <code>data_stores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.data_stores" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_stores', value: 'view', },
        { label: 'data_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the object. |
| <CopyableCode code="name" /> | `text` | Name of the object. |
| <CopyableCode code="customer_secrets" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_store_type_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | Data Store for sources and sinks |
| <CopyableCode code="type" /> | `string` | Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataStoreName, resourceGroupName, subscriptionId" /> | This method gets the data store/repository by name. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Gets all the data stores/repositories in the given resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataManagerName, dataStoreName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the data store/repository in the data manager. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerName, dataStoreName, resourceGroupName, subscriptionId" /> | This method deletes the given data store/repository. |

## `SELECT` examples

Gets all the data stores/repositories in the given resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_stores', value: 'view', },
        { label: 'data_stores', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
customer_secrets,
dataManagerName,
dataStoreName,
data_store_type_id,
extended_properties,
repository_id,
resourceGroupName,
state,
subscriptionId,
type
FROM azure.hybrid_data_manager.vw_data_stores
WHERE dataManagerName = '{{ dataManagerName }}'
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
FROM azure.hybrid_data_manager.data_stores
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_stores</code> resource.

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
INSERT INTO azure.hybrid_data_manager.data_stores (
dataManagerName,
dataStoreName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ dataManagerName }}',
'{{ dataStoreName }}',
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
    - name: name
      value: string
    - name: id
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: repositoryId
          value: string
        - name: state
          value: string
        - name: extendedProperties
          value: object
        - name: dataStoreTypeId
          value: string
        - name: customerSecrets
          value:
            - - name: keyIdentifier
                value: string
              - name: keyValue
                value: string
              - name: algorithm
                value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_stores</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_data_manager.data_stores
WHERE dataManagerName = '{{ dataManagerName }}'
AND dataStoreName = '{{ dataStoreName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
