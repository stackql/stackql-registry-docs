---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_images', value: 'view', },
        { label: 'images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hibernate_support" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommended_machine_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an image. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, imageName, resourceGroupName, subscriptionId" /> | Gets a gallery image. |
| <CopyableCode code="get_by_project" /> | `SELECT` | <CopyableCode code="imageName, projectName, resourceGroupName, subscriptionId" /> | Gets an image. |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists images for a devcenter. |
| <CopyableCode code="list_by_gallery" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, resourceGroupName, subscriptionId" /> | Lists images for a gallery. |
| <CopyableCode code="list_by_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Lists images for a project. |

## `SELECT` examples

Lists images for a project.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_images', value: 'view', },
        { label: 'images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
devCenterName,
galleryName,
hibernate_support,
imageName,
offer,
projectName,
provisioning_state,
publisher,
recommended_machine_configuration,
resourceGroupName,
sku,
subscriptionId
FROM azure.dev_center.vw_images
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.dev_center.images
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

