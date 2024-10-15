---
title: virtual_machine_extension_images
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_extension_images
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_extension_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_extension_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_extension_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_extension_images', value: 'view', },
        { label: 'virtual_machine_extension_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="compute_role" /> | `text` | field from the `properties` object |
| <CopyableCode code="handler_schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="operating_system" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="supports_multiple_extensions" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_scale_set_enabled" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine Extension Image. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, publisherName, subscriptionId, type, version" /> | Gets a virtual machine extension image. |

## `SELECT` examples

Gets a virtual machine extension image.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_extension_images', value: 'view', },
        { label: 'virtual_machine_extension_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
compute_role,
handler_schema,
location,
operating_system,
publisherName,
subscriptionId,
supports_multiple_extensions,
tags,
type,
version,
vm_scale_set_enabled
FROM azure.compute.vw_virtual_machine_extension_images
WHERE location = '{{ location }}'
AND publisherName = '{{ publisherName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND type = '{{ type }}'
AND version = '{{ version }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.compute.virtual_machine_extension_images
WHERE location = '{{ location }}'
AND publisherName = '{{ publisherName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND type = '{{ type }}'
AND version = '{{ version }}';
```
</TabItem></Tabs>

