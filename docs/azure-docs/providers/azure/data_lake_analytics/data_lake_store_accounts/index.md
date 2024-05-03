---
title: data_lake_store_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_store_accounts
  - data_lake_analytics
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
<tr><td><b>Name</b></td><td><code>data_lake_store_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.data_lake_store_accounts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The Data Lake Store account properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Store account details in the specified Data Lake Analytics account. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the first page of Data Lake Store accounts linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any. |
| <CopyableCode code="add" /> | `INSERT` | <CopyableCode code="accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId" /> | Updates the specified Data Lake Analytics account to include the additional Data Lake Store account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, dataLakeStoreAccountName, resourceGroupName, subscriptionId" /> | Updates the Data Lake Analytics account specified to remove the specified Data Lake Store account. |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the first page of Data Lake Store accounts linked to the specified Data Lake Analytics account. The response includes a link to the next page, if any. |
