---
title: account_detectors
hide_title: false
hide_table_of_contents: false
keywords:
  - account_detectors
  - batch
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

Creates, updates, deletes, gets or lists a <code>account_detectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_detectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.batch.account_detectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_account_detectors', value: 'view', },
        { label: 'account_detectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The ID of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="detectorId" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | The ETag of the resource, used for concurrency statements. |
| <CopyableCode code="properties" /> | `object` | Detector response properties. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, detectorId, resourceGroupName, subscriptionId" /> | Gets information about the given detector for a given Batch account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets information about the detectors available for a given Batch account. |

## `SELECT` examples

Gets information about the detectors available for a given Batch account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_account_detectors', value: 'view', },
        { label: 'account_detectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
detectorId,
etag,
resourceGroupName,
subscriptionId,
tags,
type,
value
FROM azure.batch.vw_account_detectors
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
tags,
type
FROM azure.batch.account_detectors
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>

