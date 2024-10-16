---
title: virtual_networks_ddos_protection_status
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_networks_ddos_protection_status
  - network
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>virtual_networks_ddos_protection_status</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_networks_ddos_protection_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_networks_ddos_protection_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ddosProtectionPlanId" /> | `string` | DDoS protection plan Resource Id of a if IP address is protected through a plan. |
| <CopyableCode code="isWorkloadProtected" /> | `string` | Value indicating whether the IP address is DDoS workload protected or not. |
| <CopyableCode code="publicIpAddress" /> | `string` | IP Address of the Public IP Resource |
| <CopyableCode code="publicIpAddressId" /> | `string` | Public IP ARM resource ID |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkName" /> | Gets the Ddos Protection Status of all IP Addresses under the Virtual Network |

## `SELECT` examples

Gets the Ddos Protection Status of all IP Addresses under the Virtual Network


```sql
SELECT
ddosProtectionPlanId,
isWorkloadProtected,
publicIpAddress,
publicIpAddressId
FROM azure.network.virtual_networks_ddos_protection_status
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkName = '{{ virtualNetworkName }}';
```