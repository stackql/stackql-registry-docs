---
title: targets
hide_title: false
hide_table_of_contents: false
keywords:
  - targets
  - chaos
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.chaos.targets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | Location of the target resource. |
| <CopyableCode code="properties" /> | `object` | Model that represents the base Target properties model. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName" /> | Get a Target resource that extends a tracked regional resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId" /> | Get a list of Target resources that extend a tracked regional resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName, data__properties" /> | Create or update a Target resource that extends a tracked regional resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName" /> | Delete a Target resource that extends a tracked regional resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId" /> | Get a list of Target resources that extend a tracked regional resource. |
