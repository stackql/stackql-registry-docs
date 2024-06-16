---
title: access_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policies
  - time_series_insights
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
<tr><td><b>Name</b></td><td><code>access_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.time_series_insights.access_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId" /> | Gets the access policy with the specified name in the specified environment. |
| <CopyableCode code="list_by_environment" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Lists all the available access policies associated with the environment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId, data__properties" /> | Create or update an access policy in the specified environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId" /> | Deletes the access policy with the specified name in the specified subscription, resource group, and environment |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accessPolicyName, environmentName, resourceGroupName, subscriptionId" /> | Updates the access policy with the specified name in the specified subscription, resource group, and environment. |
