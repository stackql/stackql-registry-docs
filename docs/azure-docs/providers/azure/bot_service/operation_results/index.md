---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - bot_service
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.bot_service.operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the operation returned. |
| <CopyableCode code="name" /> | `string` | The name of the operation result. |
| <CopyableCode code="startTime" /> | `string` | The time that the operation was started. |
| <CopyableCode code="status" /> | `string` | The status of the operation being performed. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationResultId, subscriptionId" /> | Get the operation result for a long running operation. |

## `SELECT` examples

Get the operation result for a long running operation.


```sql
SELECT
id,
name,
startTime,
status
FROM azure.bot_service.operation_results
WHERE operationResultId = '{{ operationResultId }}'
AND subscriptionId = '{{ subscriptionId }}';
```