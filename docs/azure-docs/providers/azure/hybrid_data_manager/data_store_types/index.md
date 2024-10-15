---
title: data_store_types
hide_title: false
hide_table_of_contents: false
keywords:
  - data_store_types
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

Creates, updates, deletes, gets or lists a <code>data_store_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_store_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.data_store_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_store_types', value: 'view', },
        { label: 'data_store_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the object. |
| <CopyableCode code="name" /> | `text` | Name of the object. |
| <CopyableCode code="dataManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataStoreTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="repository_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_data_services_as_sink" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_data_services_as_source" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | Data Store Type properties. |
| <CopyableCode code="type" /> | `string` | Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataStoreTypeName, resourceGroupName, subscriptionId" /> | Gets the data store/repository type given its name. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Gets all the data store/repository types that the resource supports. |

## `SELECT` examples

Gets all the data store/repository types that the resource supports.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_store_types', value: 'view', },
        { label: 'data_store_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
dataManagerName,
dataStoreTypeName,
repository_type,
resourceGroupName,
state,
subscriptionId,
supported_data_services_as_sink,
supported_data_services_as_source,
type
FROM azure.hybrid_data_manager.vw_data_store_types
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
FROM azure.hybrid_data_manager.data_store_types
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

