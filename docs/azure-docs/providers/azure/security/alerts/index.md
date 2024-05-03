---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | describes security alert properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | List all the alerts that are associated with the subscription |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List all the alerts that are associated with the resource group |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | List all the alerts that are associated with the subscription |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | List all the alerts that are associated with the resource group |
| <CopyableCode code="simulate" /> | `EXEC` | <CopyableCode code="api-version, ascLocation, subscriptionId" /> | Simulate security alerts |
