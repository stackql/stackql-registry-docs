---
title: workflow_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_triggers
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
<tr><td><b>Name</b></td><td><code>workflow_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow trigger name. |
| <CopyableCode code="properties" /> | `object` | The workflow trigger properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow trigger type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Gets a workflow trigger. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Gets a list of workflow triggers. |
| <CopyableCode code="reset" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Resets a workflow trigger. |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, workflowName" /> | Runs a workflow trigger. |
| <CopyableCode code="set_state" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, triggerName, workflowName, data__source" /> | Sets the state of a workflow trigger. |
