---
title: project_environment_types
hide_title: false
hide_table_of_contents: false
keywords:
  - project_environment_types
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
<tr><td><b>Name</b></td><td><code>project_environment_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.project_environment_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location for the environment type |
| <CopyableCode code="properties" /> | `object` | Properties of a project environment type. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Gets a project environment type. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Lists environment types for a project. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Creates or updates a project environment type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Deletes a project environment type. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="projectName, resourceGroupName, subscriptionId" /> | Lists environment types for a project. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="environmentTypeName, projectName, resourceGroupName, subscriptionId" /> | Partially updates a project environment type. |
