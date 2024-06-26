---
title: virtual_networks_ddos_protection_status
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks_ddos_protection_status
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_networks_ddos_protection_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_networks_ddos_protection_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ddosProtectionPlanId" /> | `string` |  DDoS protection plan Resource Id of a if IP address is protected through a plan. |
| <CopyableCode code="isWorkloadProtected" /> | `string` | Value indicating whether the IP address is DDoS workload protected or not. |
| <CopyableCode code="publicIpAddress" /> | `string` | IP Address of the Public IP Resource |
| <CopyableCode code="publicIpAddressId" /> | `string` | Public IP ARM resource ID |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> |
