---
title: community_galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - community_galleries
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

Creates, updates, deletes, gets or lists a <code>community_galleries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>community_galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.community_galleries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_galleries', value: 'view', },
        { label: 'community_galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="artifact_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="community_metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="disclaimer" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="publicGalleryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identifier" /> | `object` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a community gallery. |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, publicGalleryName, subscriptionId" /> | Get a community gallery by gallery public name. |

## `SELECT` examples

Get a community gallery by gallery public name.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_community_galleries', value: 'view', },
        { label: 'community_galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
artifact_tags,
community_metadata,
disclaimer,
identifier,
location,
publicGalleryName,
subscriptionId,
type
FROM azure.compute.vw_community_galleries
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
FROM azure.compute.community_galleries
WHERE location = '{{ location }}'
AND publicGalleryName = '{{ publicGalleryName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

