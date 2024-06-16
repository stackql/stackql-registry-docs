---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - vmware_cloud_simple
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.virtual_machines" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/virtualMachines/&#123;virtualMachineName&#125; |
| <CopyableCode code="name" /> | `string` | &#123;virtualMachineName&#125; |
| <CopyableCode code="location" /> | `string` | Azure region |
| <CopyableCode code="properties" /> | `object` | Properties of virtual machine |
| <CopyableCode code="tags" /> | `object` | Tags model |
| <CopyableCode code="type" /> | `string` | &#123;resourceProviderNamespace&#125;/&#123;resourceType&#125; |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineName" /> | Get virtual machine |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Returns list of virtual machine within resource group |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Returns list virtual machine within subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName, data__location" /> | Create Or Update Virtual Machine |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName" /> | Delete virtual machine |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName" /> | Power on virtual machine |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="Referer, api-version, resourceGroupName, subscriptionId, virtualMachineName" /> | Power off virtual machine, options: shutdown, poweroff, and suspend |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, virtualMachineName" /> | Patch virtual machine properties |
