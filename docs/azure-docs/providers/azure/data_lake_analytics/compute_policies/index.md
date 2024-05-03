---
title: compute_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - compute_policies
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
<tr><td><b>Name</b></td><td><code>compute_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_lake_analytics.compute_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="properties" /> | `object` | The compute policy properties. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId" /> | Gets the specified Data Lake Analytics compute policy. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Data Lake Analytics compute policies within the specified Data Lake Analytics account. An account supports, at most, 50 policies |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates the specified compute policy. During update, the compute policy with the specified name will be replaced with this new compute policy. An account supports, at most, 50 policies |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId" /> | Deletes the specified compute policy from the specified Data Lake Analytics account |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Data Lake Analytics compute policies within the specified Data Lake Analytics account. An account supports, at most, 50 policies |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, computePolicyName, resourceGroupName, subscriptionId" /> | Updates the specified compute policy. |
