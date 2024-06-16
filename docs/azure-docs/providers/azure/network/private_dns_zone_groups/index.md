---
title: private_dns_zone_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - private_dns_zone_groups
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
<tr><td><b>Name</b></td><td><code>private_dns_zone_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.private_dns_zone_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the private dns zone group. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId" /> | Gets the private dns zone group resource by specified private dns zone group name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateEndpointName, resourceGroupName, subscriptionId" /> | Gets all private dns zone groups in a private endpoint. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId" /> | Creates or updates a private dns zone group in the specified private endpoint. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateDnsZoneGroupName, privateEndpointName, resourceGroupName, subscriptionId" /> | Deletes the specified private dns zone group. |
