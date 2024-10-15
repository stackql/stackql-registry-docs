---
title: operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_status
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

Creates, updates, deletes, gets or lists a <code>operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Operation resource ID. |
| <CopyableCode code="name" /> | `string` | Operation identifier. |
| <CopyableCode code="endTime" /> | `string` | Operation end time. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="startTime" /> | `string` | Operation start time. |
| <CopyableCode code="status" /> | `string` | Operation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, assetName, operationId, resourceGroupName, subscriptionId, trackName" /> | Get asset track operation status. |

## `SELECT` examples

Get asset track operation status.


```sql
SELECT
id,
name,
endTime,
error,
startTime,
status
FROM azure.media_services.operation_status
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND trackName = '{{ trackName }}';
```