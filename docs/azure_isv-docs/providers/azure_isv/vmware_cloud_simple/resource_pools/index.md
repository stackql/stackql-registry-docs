---
title: resource_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_pools
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

Creates, updates, deletes, gets or lists a <code>resource_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.resource_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_pools', value: 'view', },
        { label: 'resource_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | resource pool id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `text` | {ResourcePoolName} |
| <CopyableCode code="full_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Azure region |
| <CopyableCode code="pcName" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_cloud_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="regionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourcePoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | {resourceProviderNamespace}/{resourceType} |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | resource pool id (privateCloudId:vsphereId) |
| <CopyableCode code="name" /> | `string` | {ResourcePoolName} |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="privateCloudId" /> | `string` | The Private Cloud Id |
| <CopyableCode code="properties" /> | `object` | Properties of resource pool |
| <CopyableCode code="type" /> | `string` | {resourceProviderNamespace}/{resourceType} |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="pcName, regionId, resourcePoolName, subscriptionId" /> | Returns resource pool templates by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="pcName, regionId, subscriptionId" /> | Returns list of resource pools in region for private cloud |

## `SELECT` examples

Returns list of resource pools in region for private cloud

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_resource_pools', value: 'view', },
        { label: 'resource_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
full_name,
location,
pcName,
private_cloud_id,
regionId,
resourcePoolName,
subscriptionId,
type
FROM azure_isv.vmware_cloud_simple.vw_resource_pools
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
privateCloudId,
properties,
type
FROM azure_isv.vmware_cloud_simple.resource_pools
WHERE pcName = '{{ pcName }}'
AND regionId = '{{ regionId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

