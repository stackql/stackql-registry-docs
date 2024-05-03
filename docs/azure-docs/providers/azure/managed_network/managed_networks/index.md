---
title: managed_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_networks
  - managed_network
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
<tr><td><b>Name</b></td><td><code>managed_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.managed_networks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of Managed Network |
| <CopyableCode code="tags" /> | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group and Managed Network name |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The ListByResourceGroup ManagedNetwork operation retrieves all the Managed Network resources in a resource group in a paginated format. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The ListBySubscription  ManagedNetwork operation retrieves all the Managed Network Resources in the current subscription in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The Put ManagedNetworks operation creates/updates a Managed Network Resource, specified by resource group and Managed Network name |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The Delete ManagedNetworks operation deletes a Managed Network Resource, specified by the  resource group and Managed Network name |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The ListByResourceGroup ManagedNetwork operation retrieves all the Managed Network resources in a resource group in a paginated format. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The ListBySubscription  ManagedNetwork operation retrieves all the Managed Network Resources in the current subscription in a paginated format. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | Updates the specified Managed Network resource tags. |
