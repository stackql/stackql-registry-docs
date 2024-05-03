---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="identity" /> | `object` | The Managed Identity of the resource |
| <CopyableCode code="location" /> | `string` | Gets or sets the location. |
| <CopyableCode code="properties" /> | `object` | The account properties |
| <CopyableCode code="sku" /> | `object` | Gets or sets the Sku. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Tags on the azure resource. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Get an account |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List accounts in ResourceGroup |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List accounts in Subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Creates or updates an account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Deletes an account resource |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List accounts in ResourceGroup |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | List accounts in Subscription |
| <CopyableCode code="add_root_collection_admin" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Add the administrator for root collection associated with this account. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Checks if account name is available. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Updates an account |
