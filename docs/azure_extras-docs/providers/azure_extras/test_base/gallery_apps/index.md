---
title: gallery_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_apps
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

Creates, updates, deletes, gets or lists a <code>gallery_apps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.gallery_apps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_apps', value: 'view', },
        { label: 'gallery_apps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="application_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="galleryAppName" /> | `text` | field from the `properties` object |
| <CopyableCode code="popularity" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a gallery application. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryAppName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets a gallery application to prepare a test run for a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all gallery applications currently available for test runs under a Test Base Account which matches user query. |

## `SELECT` examples

Lists all gallery applications currently available for test runs under a Test Base Account which matches user query.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_gallery_apps', value: 'view', },
        { label: 'gallery_apps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
application_id,
application_name,
application_type,
galleryAppName,
popularity,
provisioning_state,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_gallery_apps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.gallery_apps
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

