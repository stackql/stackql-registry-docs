---
title: public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - public_keys
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

Creates, updates, deletes, gets or lists a <code>public_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.public_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_keys', value: 'view', },
        { label: 'public_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Id of the object. |
| <CopyableCode code="name" /> | `text` | Name of the object. |
| <CopyableCode code="dataManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_service_level1_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_service_level2_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="publicKeyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the object. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Id of the object. |
| <CopyableCode code="name" /> | `string` | Name of the object. |
| <CopyableCode code="properties" /> | `object` | PublicKey Properties |
| <CopyableCode code="type" /> | `string` | Type of the object. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, publicKeyName, resourceGroupName, subscriptionId" /> | This method gets the public keys. |
| <CopyableCode code="list_by_data_manager" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | This method gets the list view of public keys, however it will only have one element. |

## `SELECT` examples

This method gets the list view of public keys, however it will only have one element.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_public_keys', value: 'view', },
        { label: 'public_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
dataManagerName,
data_service_level1_key,
data_service_level2_key,
publicKeyName,
resourceGroupName,
subscriptionId,
type
FROM azure.hybrid_data_manager.vw_public_keys
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
FROM azure.hybrid_data_manager.public_keys
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

