---
title: community_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_images
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

Creates, updates, deletes, gets or lists a <code>community_gallery_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>community_gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.community_gallery_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_gallery_images', value: 'view', },
        { label: 'community_gallery_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="architecture" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifact_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="disallowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="disclaimer" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_life_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="eula" /> | `text` | field from the `properties` object |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="os_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="privacy_statement_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="publicGalleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommended" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identifier" /> | `object` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image definition. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, location, publicGalleryName, subscriptionId" /> | Get a community gallery image. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, publicGalleryName, subscriptionId" /> | List community gallery images inside a gallery. |

## `SELECT` examples

List community gallery images inside a gallery.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_gallery_images', value: 'view', },
        { label: 'community_gallery_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
architecture,
artifact_tags,
disallowed,
disclaimer,
end_of_life_date,
eula,
features,
galleryImageName,
hyper_v_generation,
identifier,
location,
os_state,
os_type,
privacy_statement_uri,
publicGalleryName,
purchase_plan,
recommended,
subscriptionId,
type
FROM azure.compute.vw_community_gallery_images
WHERE location = '{{ location }}'
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
FROM azure.compute.community_gallery_images
WHERE location = '{{ location }}'
AND publicGalleryName = '{{ publicGalleryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

