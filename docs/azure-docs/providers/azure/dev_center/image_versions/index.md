---
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
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

Creates, updates, deletes, gets or lists a <code>image_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.image_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_image_versions', value: 'view', },
        { label: 'image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="exclude_from_latest" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="imageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_disk_image_size_in_gb" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="published_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="versionName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of an image version. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, imageName, resourceGroupName, subscriptionId, versionName" /> | Gets an image version. |
| <CopyableCode code="get_by_project" /> | `SELECT` | <CopyableCode code="imageName, projectName, resourceGroupName, subscriptionId, versionName" /> | Gets an image version. |
| <CopyableCode code="list_by_image" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, imageName, resourceGroupName, subscriptionId" /> | Lists versions for an image. |
| <CopyableCode code="list_by_project" /> | `SELECT` | <CopyableCode code="imageName, projectName, resourceGroupName, subscriptionId" /> | Lists versions for an image. |

## `SELECT` examples

Lists versions for an image.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_image_versions', value: 'view', },
        { label: 'image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
devCenterName,
exclude_from_latest,
galleryName,
imageName,
os_disk_image_size_in_gb,
projectName,
provisioning_state,
published_date,
resourceGroupName,
subscriptionId,
versionName
FROM azure.dev_center.vw_image_versions
WHERE imageName = '{{ imageName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.dev_center.image_versions
WHERE imageName = '{{ imageName }}'
AND projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

