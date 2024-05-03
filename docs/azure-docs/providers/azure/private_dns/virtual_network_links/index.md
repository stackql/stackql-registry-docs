---
title: virtual_network_links
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_links
  - private_dns
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
<tr><td><b>Name</b></td><td><code>virtual_network_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.private_dns.virtual_network_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the virtual network link. |
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the Private DNS zone. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Gets a virtual network link to the specified Private DNS zone. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Lists the virtual network links to the specified Private DNS zone. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Creates or updates a virtual network link to the specified Private DNS zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Deletes a virtual network link to the specified Private DNS zone. WARNING: In case of a registration virtual network, all auto-registered DNS records in the zone for the virtual network will also be deleted. This operation cannot be undone. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Lists the virtual network links to the specified Private DNS zone. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId, virtualNetworkLinkName" /> | Updates a virtual network link to the specified Private DNS zone. |
