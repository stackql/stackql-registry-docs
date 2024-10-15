---
title: shared_galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_galleries
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

Creates, updates, deletes, gets or lists a <code>shared_galleries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.shared_galleries" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_galleries', value: 'view', },
        { label: 'shared_galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="artifact_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryUniqueName" /> | `text` | field from the `properties` object |
| <CopyableCode code="identifier" /> | `text` | The identifier information of shared gallery. |
| <CopyableCode code="location" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identifier" /> | `object` | The identifier information of shared gallery. |
| <CopyableCode code="properties" /> | `object` | Specifies the properties of a shared gallery |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryUniqueName, location, subscriptionId" /> | Get a shared gallery by subscription id or tenant id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List shared galleries by subscription id or tenant id. |

## `SELECT` examples

List shared galleries by subscription id or tenant id.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_galleries', value: 'view', },
        { label: 'shared_galleries', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
artifact_tags,
galleryUniqueName,
identifier,
location,
subscriptionId
FROM azure.compute.vw_shared_galleries
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identifier,
properties
FROM azure.compute.shared_galleries
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

