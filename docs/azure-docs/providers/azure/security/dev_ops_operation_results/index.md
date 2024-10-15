---
title: dev_ops_operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_ops_operation_results
  - security
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

Creates, updates, deletes, gets or lists a <code>dev_ops_operation_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dev_ops_operation_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.dev_ops_operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID for the async operation. |
| <CopyableCode code="name" /> | `string` | Name of the async operation. |
| <CopyableCode code="endTime" /> | `string` | The end time of the operation. |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="operations" /> | `array` | The operations list. |
| <CopyableCode code="percentComplete" /> | `number` | Percent of the operation that is complete. |
| <CopyableCode code="resourceId" /> | `string` | Fully qualified ID of the resource against which the original async operation was started. |
| <CopyableCode code="startTime" /> | `string` | The start time of the operation. |
| <CopyableCode code="status" /> | `string` | Operation status. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationResultId, resourceGroupName, securityConnectorName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
endTime,
error,
operations,
percentComplete,
resourceId,
startTime,
status
FROM azure.security.dev_ops_operation_results
WHERE operationResultId = '{{ operationResultId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND securityConnectorName = '{{ securityConnectorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```