---
title: domains
hide_title: false
hide_table_of_contents: false
keywords:
  - domains
  - app_service
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
<tr><td><b>Name</b></td><td><code>domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.domains" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Domain resource specific properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Get a domain. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for Get all domains in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for Get all domains in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Creates or updates a domain. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Delete a domain. |
| <CopyableCode code="check_availability" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for Check if a domain is available for registration. |
| <CopyableCode code="renew" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Renew a domain. |
| <CopyableCode code="transfer_out" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="domainName, resourceGroupName, subscriptionId" /> | Description for Creates or updates a domain. |
