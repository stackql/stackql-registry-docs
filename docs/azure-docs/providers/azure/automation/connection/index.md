---
title: connection
hide_title: false
hide_table_of_contents: false
keywords:
  - connection
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
<tr><td><b>Name</b></td><td><code>connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.connection" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, connectionName, resourceGroupName, subscriptionId" /> | Retrieve the connection identified by connection name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of connections. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, connectionName, resourceGroupName, subscriptionId, data__name, data__properties" /> | Create or update a connection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, connectionName, resourceGroupName, subscriptionId" /> | Delete the connection. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="automationAccountName, connectionName, resourceGroupName, subscriptionId" /> | Update a connection. |
