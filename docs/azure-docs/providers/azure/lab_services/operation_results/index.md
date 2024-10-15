---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - lab_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="endTime" /> | `string` | End time |
| <CopyableCode code="error" /> | `object` | The error detail. |
| <CopyableCode code="percentComplete" /> | `number` | Percent completion |
| <CopyableCode code="startTime" /> | `string` | Start time |
| <CopyableCode code="status" /> | `string` | The operation status |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationResultId, subscriptionId" /> | Returns an azure operation result. |

## `SELECT` examples

Returns an azure operation result.


```sql
SELECT
id,
name,
endTime,
error,
percentComplete,
startTime,
status
FROM azure.lab_services.operation_results
WHERE operationResultId = '{{ operationResultId }}'
AND subscriptionId = '{{ subscriptionId }}';
```