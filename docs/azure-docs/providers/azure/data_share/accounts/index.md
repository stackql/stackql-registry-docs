---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_share
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity of resource |
| <CopyableCode code="location" /> | `string` | Location of the azure resource. |
| <CopyableCode code="properties" /> | `object` | Account property bag. |
| <CopyableCode code="tags" /> | `object` | Tags on the azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Get an account |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List Accounts in ResourceGroup |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List Accounts in Subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId, data__identity" /> | Create an account |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | DeleteAccount |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List Accounts in ResourceGroup |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | List Accounts in Subscription |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, api-version, resourceGroupName, subscriptionId" /> | Patch an account |
