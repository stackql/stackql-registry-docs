---
title: virtual_hub_ip_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_ip_configuration
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
<tr><td><b>Name</b></td><td><code>virtual_hub_ip_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_hub_ip_configuration" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the Ip Configuration. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of IP configuration. |
| <CopyableCode code="type" /> | `string` | Ipconfiguration type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="ipConfigName, resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of a Virtual Hub Ip configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualHubName" /> | Retrieves the details of all VirtualHubIpConfigurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="ipConfigName, resourceGroupName, subscriptionId, virtualHubName" /> | Creates a VirtualHubIpConfiguration resource if it doesn't exist else updates the existing VirtualHubIpConfiguration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="ipConfigName, resourceGroupName, subscriptionId, virtualHubName" /> | Deletes a VirtualHubIpConfiguration. |
