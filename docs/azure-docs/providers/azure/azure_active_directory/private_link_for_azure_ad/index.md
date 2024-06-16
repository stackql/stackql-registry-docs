---
title: private_link_for_azure_ad
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_for_azure_ad
  - azure_active_directory
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
<tr><td><b>Name</b></td><td><code>private_link_for_azure_ad</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.azure_active_directory.private_link_for_azure_ad" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="allTenants" /> | `boolean` | Flag indicating whether all tenants are allowed |
| <CopyableCode code="ownerTenantId" /> | `string` | Guid of the owner tenant |
| <CopyableCode code="resourceGroup" /> | `string` | Name of the resource group |
| <CopyableCode code="resourceName" /> | `string` | Name of the private link policy resource |
| <CopyableCode code="subscriptionId" /> | `string` | Subscription Identifier |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="tenants" /> | `array` | The list of tenantIds. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Gets a private link policy with a given name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Operation to return the list of Private Link Policies For AzureAD scoped to the resourceGroup. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all  Private Link Policies For AzureAD in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Creates a private link policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Deletes a private link policy. When operation completes, status code 200 returned without content. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="policyName, resourceGroupName, subscriptionId" /> | Updates private link policy tags with specified values. |
