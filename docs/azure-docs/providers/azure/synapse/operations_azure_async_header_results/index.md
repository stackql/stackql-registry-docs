---
title: operations_azure_async_header_results
hide_title: false
hide_table_of_contents: false
keywords:
  - operations_azure_async_header_results
  - synapse
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

Creates, updates, deletes, gets or lists a <code>operations_azure_async_header_results</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>operations_azure_async_header_results</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.operations_azure_async_header_results" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Operation ID |
| <CopyableCode code="name" /> | `string` | Operation name |
| <CopyableCode code="endTime" /> | `string` | Operation start time |
| <CopyableCode code="error" /> | `object` | Error details |
| <CopyableCode code="percentComplete" /> | `number` | Completion percentage of the operation |
| <CopyableCode code="properties" /> | `object` | Operation properties |
| <CopyableCode code="startTime" /> | `string` | Operation start time |
| <CopyableCode code="status" /> | `string` | Operation status |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="operationId, resourceGroupName, subscriptionId, workspaceName" /> | Get the status of an operation |

## `SELECT` examples

Get the status of an operation


```sql
SELECT
id,
name,
endTime,
error,
percentComplete,
properties,
startTime,
status
FROM azure.synapse.operations_azure_async_header_results
WHERE operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```