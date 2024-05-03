---
title: private_endpoint_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections
  - automation
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.private_endpoint_connections" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Gets a private endpoint connection. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | List all private endpoint connections on a Automation account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Approve or reject a private endpoint connection with a given name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, privateEndpointConnectionName, resourceGroupName, subscriptionId" /> | Deletes a private endpoint connection with a given name. |
| <CopyableCode code="_list_by_automation_account" /> | `EXEC` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | List all private endpoint connections on a Automation account. |
