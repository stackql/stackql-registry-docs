---
title: configuration_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_assignments
  - maintenance
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
<tr><td><b>Name</b></td><td><code>configuration_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.configuration_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | Location of the resource |
| <CopyableCode code="properties" /> | `object` | Properties for configuration assignment |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Get configuration assignment for resource.. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | List configurationAssignments for resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Register configuration for resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationAssignmentName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Unregister configuration for resource. |
