---
title: default_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - default_accounts
  - purview
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
<tr><td><b>Name</b></td><td><code>default_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.default_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountName" /> | `string` | The name of the account that is set as the default. |
| <CopyableCode code="resourceGroupName" /> | `string` | The resource group name of the account that is set as the default. |
| <CopyableCode code="scope" /> | `string` | The scope object ID. For example, sub ID or tenant ID. |
| <CopyableCode code="scopeTenantId" /> | `string` | The scope tenant in which the default account is set. |
| <CopyableCode code="scopeType" /> | `string` | The scope where the default account is set. |
| <CopyableCode code="subscriptionId" /> | `string` | The subscription ID of the account that is set as the default. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, scopeTenantId, scopeType" /> | Get the default account for the scope. |
| <CopyableCode code="remove" /> | `EXEC` | <CopyableCode code="api-version, scopeTenantId, scopeType" /> | Removes the default account from the scope. |
| <CopyableCode code="set" /> | `EXEC` | <CopyableCode code="api-version" /> | Sets the default account for the scope. |
