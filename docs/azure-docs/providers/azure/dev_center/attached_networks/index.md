---
title: attached_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_networks
  - dev_center
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
<tr><td><b>Name</b></td><td><code>attached_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.attached_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of an attached NetworkConnection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists the attached NetworkConnections for a DevCenter. |
| <CopyableCode code="list_by_project" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Lists the attached NetworkConnections for a Project. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="attachedNetworkConnectionName, devCenterName, resourceGroupName, subscriptionId" /> | Creates or updates an attached NetworkConnection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attachedNetworkConnectionName, devCenterName, resourceGroupName, subscriptionId" /> | Un-attach a NetworkConnection. |
| <CopyableCode code="get_by_dev_center" /> | `EXEC` | <CopyableCode code="attachedNetworkConnectionName, devCenterName, resourceGroupName, subscriptionId" /> | Gets an attached NetworkConnection. |
| <CopyableCode code="get_by_project" /> | `EXEC` | <CopyableCode code="attachedNetworkConnectionName, projectName, resourceGroupName, subscriptionId" /> | Gets an attached NetworkConnection. |
