---
title: public_ip_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - public_ip_addresses
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
<tr><td><b>Name</b></td><td><code>public_ip_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.public_ip_addresses" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Public IP address properties. |
| <CopyableCode code="sku" /> | `object` | SKU of a public IP address. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting the IP allocated for the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Gets the specified public IP address in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all public IP addresses in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Creates or updates a static or dynamic public IP address. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Deletes the specified public IP address. |
| <CopyableCode code="ddos_protection_status" /> | `EXEC` | <CopyableCode code="publicIpAddressName, resourceGroupName, subscriptionId" /> | Gets the Ddos Protection Status of a Public IP Address |
