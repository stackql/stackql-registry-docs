---
title: script_execution_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - script_execution_histories
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

Creates, updates, deletes, gets or lists a <code>script_execution_histories</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>script_execution_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hdinsight.script_execution_histories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the script action. |
| <CopyableCode code="applicationName" /> | `string` | The application name of the script action, if any. |
| <CopyableCode code="debugInformation" /> | `string` | The script action execution debug information. |
| <CopyableCode code="endTime" /> | `string` | The end time of script action execution. |
| <CopyableCode code="executionSummary" /> | `array` | The summary of script action execution result. |
| <CopyableCode code="operation" /> | `string` | The reason why the script action was executed. |
| <CopyableCode code="parameters" /> | `string` | The parameters for the script |
| <CopyableCode code="roles" /> | `array` | The list of roles where script will be executed. |
| <CopyableCode code="scriptExecutionId" /> | `integer` | The execution id of the script action. |
| <CopyableCode code="startTime" /> | `string` | The start time of script action execution. |
| <CopyableCode code="status" /> | `string` | The current execution status of the script action. |
| <CopyableCode code="uri" /> | `string` | The URI to the script. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Lists all scripts' execution history for the specified cluster. |
| <CopyableCode code="promote" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, scriptExecutionId, subscriptionId" /> | Promotes the specified ad-hoc script execution to a persisted script. |

## `SELECT` examples

Lists all scripts' execution history for the specified cluster.


```sql
SELECT
name,
applicationName,
debugInformation,
endTime,
executionSummary,
operation,
parameters,
roles,
scriptExecutionId,
startTime,
status,
uri
FROM azure.hdinsight.script_execution_histories
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```