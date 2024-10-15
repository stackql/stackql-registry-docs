---
title: shared_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_images
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

Creates, updates, deletes, gets or lists a <code>shared_gallery_images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.shared_gallery_images" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_gallery_images', value: 'view', },
        { label: 'shared_gallery_images', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="architecture" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifact_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="disallowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_of_life_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="eula" /> | `text` | field from the `properties` object |
| <CopyableCode code="features" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryImageName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryUniqueName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hyper_v_generation" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | The identifier information of shared gallery. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="privacy_statement_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="recommended" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identifier" /> | `object` | The identifier information of shared gallery. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image definition. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryUniqueName, location, subscriptionId" /> | Get a shared gallery image by subscription id or tenant id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="galleryUniqueName, location, subscriptionId" /> | List shared gallery images by subscription id or tenant id. |

## `SELECT` examples

List shared gallery images by subscription id or tenant id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_gallery_images', value: 'view', },
        { label: 'shared_gallery_images', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
architecture,
artifact_tags,
disallowed,
end_of_life_date,
eula,
features,
galleryImageName,
galleryUniqueName,
hyper_v_generation,
identifier,
location,
os_state,
os_type,
privacy_statement_uri,
purchase_plan,
recommended,
subscriptionId
FROM azure.compute.vw_shared_gallery_images
WHERE galleryUniqueName = '{{ galleryUniqueName }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identifier,
properties
FROM azure.compute.shared_gallery_images
WHERE galleryUniqueName = '{{ galleryUniqueName }}'
AND location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

