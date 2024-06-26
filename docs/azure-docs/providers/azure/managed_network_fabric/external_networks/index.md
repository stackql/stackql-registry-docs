---
title: external_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - external_networks
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
<tr><td><b>Name</b></td><td><code>external_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.external_networks" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements ExternalNetworks GET method. |
| <CopyableCode code="list_by_l3_isolation_domain" /> | `SELECT` | <CopyableCode code="l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements External Networks list by resource group GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId, data__properties" /> | Creates ExternalNetwork PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | Implements ExternalNetworks DELETE method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="externalNetworkName, l3IsolationDomainName, resourceGroupName, subscriptionId" /> | API to update certain properties of the ExternalNetworks resource. |
