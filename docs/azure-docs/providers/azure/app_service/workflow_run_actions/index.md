---
title: workflow_run_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_run_actions
  - app_service
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
<tr><td><b>Name</b></td><td><code>workflow_run_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.workflow_run_actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow run action name. |
| <CopyableCode code="properties" /> | `object` | The workflow run action properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow run action type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionName, name, resourceGroupName, runName, subscriptionId, workflowName" /> | Gets a workflow run action. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, runName, subscriptionId, workflowName" /> | Gets a list of workflow run actions. |
