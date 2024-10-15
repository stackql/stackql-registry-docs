---
title: virtual_router_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_router_peerings
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

Creates, updates, deletes, gets or lists a <code>virtual_router_peerings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_router_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_router_peerings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_router_peerings', value: 'view', },
        { label: 'virtual_router_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Name of the virtual router peering that is unique within a virtual router. |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="peer_asn" /> | `text` | field from the `properties` object |
| <CopyableCode code="peer_ip" /> | `text` | field from the `properties` object |
| <CopyableCode code="peeringName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Peering type. |
| <CopyableCode code="virtualRouterName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the virtual router peering that is unique within a virtual router. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the rule group. |
| <CopyableCode code="type" /> | `string` | Peering type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, virtualRouterName" /> | Gets the specified Virtual Router Peering. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualRouterName" /> | Lists all Virtual Router Peerings in a Virtual Router resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, virtualRouterName" /> | Creates or updates the specified Virtual Router Peering. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="peeringName, resourceGroupName, subscriptionId, virtualRouterName" /> | Deletes the specified peering from a Virtual Router. |

## `SELECT` examples

Lists all Virtual Router Peerings in a Virtual Router resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_router_peerings', value: 'view', },
        { label: 'virtual_router_peerings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
etag,
peer_asn,
peer_ip,
peeringName,
provisioning_state,
resourceGroupName,
subscriptionId,
type,
virtualRouterName
FROM azure.network.vw_virtual_router_peerings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualRouterName = '{{ virtualRouterName }}';
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
FROM azure.network.virtual_router_peerings
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualRouterName = '{{ virtualRouterName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_router_peerings</code> resource.

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
INSERT INTO azure.network.virtual_router_peerings (
peeringName,
resourceGroupName,
subscriptionId,
virtualRouterName,
properties,
name,
id
)
SELECT 
'{{ peeringName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualRouterName }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: peerAsn
          value: integer
        - name: peerIp
          value: string
        - name: provisioningState
          value: []
    - name: name
      value: string
    - name: etag
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_router_peerings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.virtual_router_peerings
WHERE peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualRouterName = '{{ virtualRouterName }}';
```
