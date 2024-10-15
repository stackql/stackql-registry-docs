---
title: live_pipeline_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - live_pipeline_operation_status
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>live_pipeline_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_pipeline_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.live_pipeline_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the live pipeline operation. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="status" /> | `string` | The status of the live pipeline operation. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, livePipelineName, operationId, resourceGroupName, subscriptionId" /> | Get the operation status of a live pipeline. |

## `SELECT` examples

Get the operation status of a live pipeline.


```sql
SELECT
name,
error,
status
FROM azure.video_analyzer.live_pipeline_operation_status
WHERE accountName = '{{ accountName }}'
AND livePipelineName = '{{ livePipelineName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```