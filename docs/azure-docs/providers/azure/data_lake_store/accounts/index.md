---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
  - data_lake_store
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_store.accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="identity" /> | `object` | The encryption identity properties. |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | Data Lake Store account properties information. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Store account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, data__location" /> | Creates the specified Data Lake Store account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Deletes the specified Data Lake Store account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__name, data__type" /> | Checks whether the specified account name is available or taken. |
| <CopyableCode code="enable_key_vault" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Updates the specified Data Lake Store account information. |
