---
title: workflow_trigger_histories
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_trigger_histories
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
<tr><td><b>Name</b></td><td><code>workflow_trigger_histories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_trigger_histories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow trigger history name. |
| <CopyableCode code="properties" /> | `object` | The workflow trigger history properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow trigger history type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, historyName, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Gets a workflow trigger history. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Gets a list of workflow trigger histories. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Gets a list of workflow trigger histories. |
| <CopyableCode code="resubmit" /> | `EXEC` | <CopyableCode code="api-version, historyName, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Resubmits a workflow run based on the trigger history. |
