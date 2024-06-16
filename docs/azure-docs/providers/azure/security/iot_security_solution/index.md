---
title: iot_security_solution
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_security_solution
  - security
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
<tr><td><b>Name</b></td><td><code>iot_security_solution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.iot_security_solution" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | Security Solution setting data |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, solutionName, subscriptionId" /> | User this method to get details of a specific IoT Security solution based on solution name |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Use this method to get the list IoT Security solutions organized by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Use this method to get the list of IoT Security solutions by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, solutionName, subscriptionId" /> | Use this method to create or update yours IoT Security solution |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, solutionName, subscriptionId" /> | Use this method to delete yours IoT Security solution |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, solutionName, subscriptionId" /> | Use this method to update existing IoT Security solution tags or user defined resources. To update other fields use the CreateOrUpdate method. |
