---
title: data_services
hide_title: false
hide_table_of_contents: false
keywords:
  - data_services
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

Creates, updates, deletes, gets or lists a <code>data_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.data_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_services', value: 'view', },
        { label: 'data_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the object. |
| <CopyableCode code="name" /> | `text` | Name of the object. |
| <CopyableCode code="dataManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_data_sink_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_data_source_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | Data Service properties. |
| <CopyableCode code="type" /> | `string` | Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, dataServiceName, resourceGroupName, subscriptionId" /> | Gets the data service that matches the data service name given. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets all the data services. |

## `SELECT` examples

This method gets all the data services.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_services', value: 'view', },
        { label: 'data_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
dataManagerName,
dataServiceName,
resourceGroupName,
state,
subscriptionId,
supported_data_sink_types,
supported_data_source_types,
type
FROM azure.hybrid_data_manager.vw_data_services
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
FROM azure.hybrid_data_manager.data_services
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

