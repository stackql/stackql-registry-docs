---
title: peering_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - peering_policies
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
<tr><td><b>Name</b></td><td><code>peering_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.peering_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId" /> | The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name |
| <CopyableCode code="list_by_managed_network" /> | `SELECT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId" /> | The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Policy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedNetworkName, managedNetworkPeeringPolicyName, resourceGroupName, subscriptionId" /> | The Delete ManagedNetworkPeeringPolicies operation deletes a Managed Network Peering Policy, specified by the  resource group, Managed Network name, and peering policy name |
| <CopyableCode code="_list_by_managed_network" /> | `EXEC` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format. |
