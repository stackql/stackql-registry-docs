---
title: workflow_run_action_repetitions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_action_repetitions
  - logic_apps
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workflow_run_action_repetitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_run_action_repetitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the resource name. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The workflow run action repetition properties definition. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionName, api-version, repetitionName, resourceGroupName, runName, subscriptionId, workflowName" /> | Get a workflow run action repetition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName" /> | Get all of a workflow run action repetitions. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="actionName, api-version, resourceGroupName, runName, subscriptionId, workflowName" /> | Get all of a workflow run action repetitions. |
