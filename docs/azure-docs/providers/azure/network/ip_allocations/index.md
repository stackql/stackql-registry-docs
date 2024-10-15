---
title: ip_allocations
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_allocations
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

Creates, updates, deletes, gets or lists a <code>ip_allocations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_allocations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.ip_allocations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_allocations', value: 'view', },
        { label: 'ip_allocations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="allocation_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="ipAllocationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ipam_allocation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="prefix" /> | `text` | field from the `properties` object |
| <CopyableCode code="prefix_length" /> | `text` | field from the `properties` object |
| <CopyableCode code="prefix_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subnet" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="virtual_network" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the IpAllocation. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipAllocationName, resourceGroupName, subscriptionId" /> | Gets the specified IpAllocation by resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all IpAllocations in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all IpAllocations in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ipAllocationName, resourceGroupName, subscriptionId" /> | Creates or updates an IpAllocation in the specified resource group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ipAllocationName, resourceGroupName, subscriptionId" /> | Deletes the specified IpAllocation. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="ipAllocationName, resourceGroupName, subscriptionId" /> | Updates a IpAllocation tags. |

## `SELECT` examples

Gets all IpAllocations in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ip_allocations', value: 'view', },
        { label: 'ip_allocations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allocation_tags,
etag,
ipAllocationName,
ipam_allocation_id,
location,
prefix,
prefix_length,
prefix_type,
resourceGroupName,
subnet,
subscriptionId,
tags,
type,
virtual_network
FROM azure.network.vw_ip_allocations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.ip_allocations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ip_allocations</code> resource.

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
INSERT INTO azure.network.ip_allocations (
ipAllocationName,
resourceGroupName,
subscriptionId,
properties,
id,
location,
tags
)
SELECT 
'{{ ipAllocationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ id }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: subnet
          value:
            - name: id
              value: string
        - name: type
          value: []
        - name: prefix
          value: string
        - name: prefixLength
          value: integer
        - name: prefixType
          value: []
        - name: ipamAllocationId
          value: string
        - name: allocationTags
          value: object
    - name: etag
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>ip_allocations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.ip_allocations
WHERE ipAllocationName = '{{ ipAllocationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
