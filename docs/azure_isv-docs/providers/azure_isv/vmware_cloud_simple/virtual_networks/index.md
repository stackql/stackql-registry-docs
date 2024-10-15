---
title: virtual_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks
  - vmware_cloud_simple
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

Creates, updates, deletes, gets or lists a <code>virtual_networks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.virtual_networks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_networks', value: 'view', },
        { label: 'virtual_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | virtual network id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `text` | {VirtualNetworkName} |
| <CopyableCode code="assignable" /> | `boolean` | can be used in vm creation/deletion |
| <CopyableCode code="location" /> | `text` | Azure region |
| <CopyableCode code="pcName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="regionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourcePoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | {resourceProviderNamespace}/{resourceType} |
| <CopyableCode code="virtualNetworkName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | virtual network id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `string` | {VirtualNetworkName} |
| <CopyableCode code="assignable" /> | `boolean` | can be used in vm creation/deletion |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of virtual network |
| <CopyableCode code="type" /> | `string` | {resourceProviderNamespace}/{resourceType} |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pcName, regionId, subscriptionId, virtualNetworkName" /> | Return virtual network by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="pcName, regionId, resourcePoolName, subscriptionId" /> | Return list of virtual networks in location for private cloud |

## `SELECT` examples

Return list of virtual networks in location for private cloud

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_networks', value: 'view', },
        { label: 'virtual_networks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
assignable,
location,
pcName,
private_cloud_id,
regionId,
resourcePoolName,
subscriptionId,
type,
virtualNetworkName
FROM azure_isv.vmware_cloud_simple.vw_virtual_networks
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND resourcePoolName = '{{ resourcePoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
assignable,
location,
properties,
type
FROM azure_isv.vmware_cloud_simple.virtual_networks
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND resourcePoolName = '{{ resourcePoolName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

