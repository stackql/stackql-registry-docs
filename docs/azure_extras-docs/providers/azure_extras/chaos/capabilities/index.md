---
title: capabilities
hide_title: false
hide_table_of_contents: false
keywords:
  - capabilities
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
<tr><td><b>Name</b></td><td><code>capabilities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.chaos.capabilities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Model that represents the Capability properties model. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, capabilityName, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName" /> | Get a Capability resource that extends a Target resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName" /> | Get a list of Capability resources that extend a Target resource.. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, capabilityName, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName" /> | Create or update a Capability resource that extends a Target resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, capabilityName, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName" /> | Delete a Capability that extends a Target resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, parentProviderNamespace, parentResourceName, parentResourceType, resourceGroupName, subscriptionId, targetName" /> | Get a list of Capability resources that extend a Target resource.. |
