---
title: connection_type
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_type
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
<tr><td><b>Name</b></td><td><code>connection_type</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automation.connection_type" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets the id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets the name of the connection type. |
| <CopyableCode code="properties" /> | `object` | Properties of the connection type. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="automationAccountName, connectionTypeName, resourceGroupName, subscriptionId" /> | Retrieve the connection type identified by connection type name. |
| <CopyableCode code="list_by_automation_account" /> | `SELECT` | <CopyableCode code="automationAccountName, resourceGroupName, subscriptionId" /> | Retrieve a list of connection types. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="automationAccountName, connectionTypeName, resourceGroupName, subscriptionId, data__name, data__properties" /> | Create a connection type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="automationAccountName, connectionTypeName, resourceGroupName, subscriptionId" /> | Delete the connection type. |
