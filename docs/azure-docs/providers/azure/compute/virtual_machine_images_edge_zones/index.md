---
title: virtual_machine_images_edge_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_images_edge_zones
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_images_edge_zones</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_images_edge_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_images_edge_zones" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_images_edge_zones', value: 'view', },
        { label: 'virtual_machine_images_edge_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="architecture" /> | `text` | field from the `properties` object |
| <CopyableCode code="automatic_os_upgrade_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_disk_images" /> | `text` | field from the `properties` object |
| <CopyableCode code="disallowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="edgeZone" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="image_deprecation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The supported Azure location of the resource. |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_disk_image" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="skus" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Specifies the tags that are assigned to the virtual machine. For more information about using tags, see [Using tags to organize your Azure resources](https://docs.microsoft.com/azure/azure-resource-manager/resource-group-using-tags.md). |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The supported Azure location of the resource. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Image. |
| <CopyableCode code="tags" /> | `object` | Specifies the tags that are assigned to the virtual machine. For more information about using tags, see [Using tags to organize your Azure resources](https://docs.microsoft.com/azure/azure-resource-manager/resource-group-using-tags.md). |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="edgeZone, location, offer, publisherName, skus, subscriptionId, version" /> | Gets a virtual machine image in an edge zone. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="edgeZone, location, offer, publisherName, skus, subscriptionId" /> | Gets a list of all virtual machine image versions for the specified location, edge zone, publisher, offer, and SKU. |

## `SELECT` examples

Gets a list of all virtual machine image versions for the specified location, edge zone, publisher, offer, and SKU.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_images_edge_zones', value: 'view', },
        { label: 'virtual_machine_images_edge_zones', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
architecture,
automatic_os_upgrade_properties,
data_disk_images,
disallowed,
edgeZone,
extended_location,
features,
hyper_v_generation,
image_deprecation_status,
location,
offer,
os_disk_image,
plan,
publisherName,
skus,
subscriptionId,
tags,
version
FROM azure.compute.vw_virtual_machine_images_edge_zones
WHERE edgeZone = '{{ edgeZone }}'
AND location = '{{ location }}'
AND offer = '{{ offer }}'
AND publisherName = '{{ publisherName }}'
AND skus = '{{ skus }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
name,
extendedLocation,
location,
properties,
tags
FROM azure.compute.virtual_machine_images_edge_zones
WHERE edgeZone = '{{ edgeZone }}'
AND location = '{{ location }}'
AND offer = '{{ offer }}'
AND publisherName = '{{ publisherName }}'
AND skus = '{{ skus }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

