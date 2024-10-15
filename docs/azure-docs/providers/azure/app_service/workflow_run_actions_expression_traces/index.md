---
title: workflow_run_actions_expression_traces
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_actions_expression_traces
  - app_service
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

Creates, updates, deletes, gets or lists a <code>workflow_run_actions_expression_traces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_run_actions_expression_traces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_run_actions_expression_traces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="inputs" /> | `array` |  |
| <CopyableCode code="nextLink" /> | `string` | The link used to get the next page of recommendations. |
| <CopyableCode code="value" /> | `` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="actionName, name, resourceGroupName, runName, subscriptionId, workflowName" /> | Lists a workflow run expression trace. |

## `SELECT` examples

Lists a workflow run expression trace.


```sql
SELECT
inputs,
nextLink,
value
FROM azure.app_service.workflow_run_actions_expression_traces
WHERE actionName = '{{ actionName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runName = '{{ runName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workflowName = '{{ workflowName }}';
```