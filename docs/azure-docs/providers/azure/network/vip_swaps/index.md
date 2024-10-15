---
title: vip_swaps
hide_title: false
hide_table_of_contents: false
keywords:
  - vip_swaps
  - network
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

Creates, updates, deletes, gets or lists a <code>vip_swaps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vip_swaps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.vip_swaps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vip_swaps', value: 'view', },
        { label: 'vip_swaps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="groupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="singletonResource" /> | `text` | field from the `properties` object |
| <CopyableCode code="slot_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Swap resource properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupName, resourceName, singletonResource, subscriptionId" /> | Gets the SwapResource which identifies the slot type for the specified cloud service. The slot type on a cloud service can either be Staging or Production |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="groupName, resourceName, subscriptionId" /> | Gets the list of SwapResource which identifies the slot type for the specified cloud service. The slot type on a cloud service can either be Staging or Production |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="groupName, resourceName, singletonResource, subscriptionId" /> | Performs vip swap operation on swappable cloud services. |

## `SELECT` examples

Gets the list of SwapResource which identifies the slot type for the specified cloud service. The slot type on a cloud service can either be Staging or Production

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_vip_swaps', value: 'view', },
        { label: 'vip_swaps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
groupName,
resourceName,
singletonResource,
slot_type,
subscriptionId,
type
FROM azure.network.vw_vip_swaps
WHERE groupName = '{{ groupName }}'
AND resourceName = '{{ resourceName }}'
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
FROM azure.network.vip_swaps
WHERE groupName = '{{ groupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vip_swaps</code> resource.

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
INSERT INTO azure.network.vip_swaps (
groupName,
resourceName,
singletonResource,
subscriptionId,
properties
)
SELECT 
'{{ groupName }}',
'{{ resourceName }}',
'{{ singletonResource }}',
'{{ subscriptionId }}',
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
        - name: slotType
          value: string

```
</TabItem>
</Tabs>
