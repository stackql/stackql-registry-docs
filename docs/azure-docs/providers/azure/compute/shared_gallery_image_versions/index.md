---
title: shared_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_image_versions
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

Creates, updates, deletes, gets or lists a <code>shared_gallery_image_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.shared_gallery_image_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_gallery_image_versions', value: 'view', },
        { label: 'shared_gallery_image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifact_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_life_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="exclude_from_latest" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageVersionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryUniqueName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | The identifier information of shared gallery. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="published_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identifier" /> | `object` | The identifier information of shared gallery. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image version. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryImageVersionName, galleryUniqueName, location, subscriptionId" /> | Get a shared gallery image version by subscription id or tenant id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryUniqueName, location, subscriptionId" /> | List shared gallery image versions by subscription id or tenant id. |

## `SELECT` examples

List shared gallery image versions by subscription id or tenant id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_gallery_image_versions', value: 'view', },
        { label: 'shared_gallery_image_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
artifact_tags,
end_of_life_date,
exclude_from_latest,
galleryImageName,
galleryImageVersionName,
galleryUniqueName,
identifier,
location,
published_date,
storage_profile,
subscriptionId
FROM azure.compute.vw_shared_gallery_image_versions
WHERE galleryImageName = '{{ galleryImageName }}'
AND galleryUniqueName = '{{ galleryUniqueName }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identifier,
properties
FROM azure.compute.shared_gallery_image_versions
WHERE galleryImageName = '{{ galleryImageName }}'
AND galleryUniqueName = '{{ galleryUniqueName }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

