---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - media_services
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

Creates, updates, deletes, gets or lists a <code>operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.operation_results" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operation_results', value: 'view', },
        { label: 'operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="operationId" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="track" /> | `text` | field from the `properties` object |
| <CopyableCode code="trackName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a video, audio or text track in the asset. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, assetName, operationId, resourceGroupName, subscriptionId, trackName" /> | Get asset track operation result. |

## `SELECT` examples

Get asset track operation result.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_operation_results', value: 'view', },
        { label: 'operation_results', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
accountName,
assetName,
operationId,
provisioning_state,
resourceGroupName,
subscriptionId,
track,
trackName
FROM azure.media_services.vw_operation_results
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trackName = '{{ trackName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.media_services.operation_results
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trackName = '{{ trackName }}';
```
</TabItem></Tabs>

