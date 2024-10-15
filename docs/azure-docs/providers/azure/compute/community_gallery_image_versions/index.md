---
title: community_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_image_versions
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

Creates, updates, deletes, gets or lists a <code>community_gallery_image_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>community_gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.community_gallery_image_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_gallery_image_versions', value: 'view', },
        { label: 'community_gallery_image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="artifact_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="disclaimer" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_life_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="exclude_from_latest" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="publicGalleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="published_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identifier" /> | `object` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image version. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryImageVersionName, location, publicGalleryName, subscriptionId" /> | Get a community gallery image version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="galleryImageName, location, publicGalleryName, subscriptionId" /> | List community gallery image versions inside an image. |

## `SELECT` examples

List community gallery image versions inside an image.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_gallery_image_versions', value: 'view', },
        { label: 'community_gallery_image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
artifact_tags,
disclaimer,
end_of_life_date,
exclude_from_latest,
galleryImageName,
galleryImageVersionName,
identifier,
location,
publicGalleryName,
published_date,
storage_profile,
subscriptionId,
type
FROM azure.compute.vw_community_gallery_image_versions
WHERE galleryImageName = '{{ galleryImageName }}'
AND location = '{{ location }}'
AND publicGalleryName = '{{ publicGalleryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
name,
identifier,
location,
properties,
type
FROM azure.compute.community_gallery_image_versions
WHERE galleryImageName = '{{ galleryImageName }}'
AND location = '{{ location }}'
AND publicGalleryName = '{{ publicGalleryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

