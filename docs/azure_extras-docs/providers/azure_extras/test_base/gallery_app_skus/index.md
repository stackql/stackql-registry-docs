---
title: gallery_app_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_app_skus
  - test_base
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

Creates, updates, deletes, gets or lists a <code>gallery_app_skus</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_app_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.gallery_app_skus" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_app_skus', value: 'view', },
        { label: 'gallery_app_skus', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="application_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryAppName" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryAppSkuName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a gallery application SKU. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryAppName, galleryAppSkuName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a gallery application SKU for test runs under a Test Base account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="galleryAppName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all SKUs of a gallery application currently available for test runs under a Test Base account. |

## `SELECT` examples

Lists all SKUs of a gallery application currently available for test runs under a Test Base account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_app_skus', value: 'view', },
        { label: 'gallery_app_skus', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
application_type,
galleryAppName,
galleryAppSkuName,
provisioning_state,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_gallery_app_skus
WHERE galleryAppName = '{{ galleryAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.gallery_app_skus
WHERE galleryAppName = '{{ galleryAppName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

