---
title: data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - data_pools
  - autonomous_dev_platform
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
<tr><td><b>Name</b></td><td><code>data_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.autonomous_dev_platform.data_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Data Pool properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Gets the properties of a Data Pool |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the data pools under the ADP account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Creates or updates a Data Pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Deletes a Data Pool |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing Data Pool |
