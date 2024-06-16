---
title: integration_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes
  - synapse
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
<tr><td><b>Name</b></td><td><code>integration_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.integration_runtimes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Get an integration runtime |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | List all integration runtimes |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Create an integration runtime |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Delete an integration runtime |
| <CopyableCode code="disable_interactive_query" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Disable interactive query in integration runtime |
| <CopyableCode code="enable_interactive_query" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Enable interactive query in integration runtime |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Start an integration runtime |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Stop an integration runtime |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Update an integration runtime |
| <CopyableCode code="upgrade" /> | `EXEC` | <CopyableCode code="integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName" /> | Upgrade an integration runtime |
