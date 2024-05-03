---
title: workflow_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - workflow_runs
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
<tr><td><b>Name</b></td><td><code>workflow_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.logic_apps.workflow_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id. |
| <CopyableCode code="name" /> | `string` | Gets the workflow run name. |
| <CopyableCode code="properties" /> | `object` | The workflow run properties. |
| <CopyableCode code="type" /> | `string` | Gets the workflow run type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, runName, subscriptionId, workflowName" /> | Gets a workflow run. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Gets a list of workflow runs. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, workflowName" /> | Gets a list of workflow runs. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, runName, subscriptionId, workflowName" /> | Cancels a workflow run. |
