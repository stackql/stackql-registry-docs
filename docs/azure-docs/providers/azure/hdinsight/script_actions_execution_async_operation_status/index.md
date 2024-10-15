---
title: script_actions_execution_async_operation_status
hide_title: false
hide_table_of_contents: false
keywords:
  - script_actions_execution_async_operation_status
  - hdinsight
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

Creates, updates, deletes, gets or lists a <code>script_actions_execution_async_operation_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>script_actions_execution_async_operation_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.script_actions_execution_async_operation_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="error" /> | `object` | The error message associated with the cluster creation. |
| <CopyableCode code="status" /> | `string` | The async operation state. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, operationId, resourceGroupName, subscriptionId" /> | Gets the async operation status of execution operation. |

## `SELECT` examples

Gets the async operation status of execution operation.


```sql
SELECT
error,
status
FROM azure.hdinsight.script_actions_execution_async_operation_status
WHERE clusterName = '{{ clusterName }}'
AND operationId = '{{ operationId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```