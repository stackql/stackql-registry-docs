---
title: virtual_network_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_addresses
  - oracle
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>virtual_network_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.virtual_network_addresses" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, virtualnetworkaddressname" /> | Get a VirtualNetworkAddress |
| <CopyableCode code="list_by_cloud_vm_cluster" /> | `SELECT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId" /> | List VirtualNetworkAddress resources by CloudVmCluster |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, virtualnetworkaddressname" /> | Create a VirtualNetworkAddress |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudvmclustername, resourceGroupName, subscriptionId, virtualnetworkaddressname" /> | Delete a VirtualNetworkAddress |
