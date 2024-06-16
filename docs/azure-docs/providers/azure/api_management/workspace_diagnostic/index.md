---
title: workspace_diagnostic
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_diagnostic
  - api_management
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
<tr><td><b>Name</b></td><td><code>workspace_diagnostic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_diagnostic" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the Diagnostic specified by its identifier. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists all diagnostics in the specified workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates a new Diagnostic or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the specified Diagnostic. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the details of the Diagnostic specified by its identifier. |
