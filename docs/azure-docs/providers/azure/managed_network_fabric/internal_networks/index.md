---
title: internal_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - internal_networks
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>internal_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.internal_networks" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Gets a InternalNetworks. |
| <CopyableCode code="list_by_l3_isolation_domain" /> | `SELECT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Displays InternalNetworks list by resource group GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Creates InternalNetwork PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements InternalNetworks DELETE method. |
| <CopyableCode code="_list_by_l3_isolation_domain" /> | `EXEC` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Displays InternalNetworks list by resource group GET method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="internalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Updates a InternalNetworks. |
