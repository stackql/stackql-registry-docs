---
title: platform_images
hide_title: false
hide_table_of_contents: false
keywords:
  - platform_images
  - compute_admin
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

Creates, updates, deletes, gets or lists a <code>platform_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>platform_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.platform_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_platform_images', value: 'view', },
        { label: 'platform_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | ID of the resource. |
| <CopyableCode code="name" /> | `text` | Name of the resource. |
| <CopyableCode code="data_disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="details" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Location of the resource. |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_disk" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of Resource. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of platform image. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, offer, publisher, sku, subscriptionId, version" /> | Returns the specific platform image matching publisher, offer, skus and version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of all platform images. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, offer, publisher, sku, subscriptionId, version" /> | Creates a new platform image with given publisher, offer, skus and version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, offer, publisher, sku, subscriptionId, version" /> | Delete a platform image |

## `SELECT` examples

Returns a list of all platform images.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_platform_images', value: 'view', },
        { label: 'platform_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
data_disks,
details,
location,
offer,
os_disk,
provisioning_state,
publisher,
sku,
subscriptionId,
type,
version
FROM azure_stack.compute_admin.vw_platform_images
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure_stack.compute_admin.platform_images
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>platform_images</code> resource.

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
INSERT INTO azure_stack.compute_admin.platform_images (
location,
offer,
publisher,
sku,
subscriptionId,
version,
properties
)
SELECT 
'{{ location }}',
'{{ offer }}',
'{{ publisher }}',
'{{ sku }}',
'{{ subscriptionId }}',
'{{ version }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: osDisk
          value:
            - name: osType
              value: []
            - name: uri
              value: string
        - name: dataDisks
          value:
            - - name: lun
                value: integer
              - name: uri
                value: string
        - name: details
          value:
            - name: billingPartNumber
              value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>platform_images</code> resource.

```sql
/*+ delete */
DELETE FROM azure_stack.compute_admin.platform_images
WHERE location = '{{ location }}'
AND offer = '{{ offer }}'
AND publisher = '{{ publisher }}'
AND sku = '{{ sku }}'
AND subscriptionId = '{{ subscriptionId }}'
AND version = '{{ version }}';
```
