---
title: operation_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operation_results
  - deployment_admin
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.deployment_admin.operation_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="endTime" /> | `string` | The deployment end time |
| <CopyableCode code="percentComplete" /> | `number` | Percentage completed. |
| <CopyableCode code="startTime" /> | `string` | The deployment start time |
| <CopyableCode code="status" /> | `string` | Specifies the state of the Operation result. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, operationResultId, subscriptionId" /> | Retrieves the specific operation results. |

## `SELECT` examples

Retrieves the specific operation results.


```sql
SELECT
id,
name,
endTime,
percentComplete,
startTime,
status
FROM azure_stack.deployment_admin.operation_results
WHERE location = '{{ location }}'
AND operationResultId = '{{ operationResultId }}'
AND subscriptionId = '{{ subscriptionId }}';
```