---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
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
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Responsibility role under which this Managed Network Group will be created |
| <CopyableCode code="properties" /> | `object` | Properties of a Managed Network Group |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managedNetworkGroupName, managedNetworkName, resourceGroupName, subscriptionId" /> | The Get ManagedNetworkGroups operation gets a Managed Network Group specified by the resource group, Managed Network name, and group name |
| <CopyableCode code="list_by_managed_network" /> | `SELECT` | <CopyableCode code="managedNetworkName, resourceGroupName, subscriptionId" /> | The ListByManagedNetwork ManagedNetworkGroup operation retrieves all the Managed Network Groups in a specified Managed Networks in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managedNetworkGroupName, managedNetworkName, resourceGroupName, subscriptionId" /> | The Put ManagedNetworkGroups operation creates or updates a Managed Network Group resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managedNetworkGroupName, managedNetworkName, resourceGroupName, subscriptionId" /> | The Delete ManagedNetworkGroups operation deletes a Managed Network Group specified by the resource group, Managed Network name, and group name |
