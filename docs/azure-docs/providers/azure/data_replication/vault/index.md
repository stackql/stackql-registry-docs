---
title: vault
hide_title: false
hide_table_of_contents: false
keywords:
  - vault
  - data_replication
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
<tr><td><b>Name</b></td><td><code>vault</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.vault" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="location" /> | `string` | Gets or sets the location of the vault. |
| <CopyableCode code="properties" /> | `object` | Vault properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="tags" /> | `object` | Gets or sets the resource tags. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the vault. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the list of vaults in the given subscription and resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the list of vaults in the given subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__location" /> | Creates the vault. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Removes the vault. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the list of vaults in the given subscription and resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets the list of vaults in the given subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Performs update on the vault. |
