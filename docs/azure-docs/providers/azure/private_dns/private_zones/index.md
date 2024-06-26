---
title: private_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - private_zones
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
<tr><td><b>Name</b></td><td><code>private_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.private_dns.private_zones" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the zone. |
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Represents the properties of the Private DNS zone. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Gets a Private DNS zone. Retrieves the zone properties, but not the virtual networks links or the record sets within the zone. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the Private DNS zones in all resource groups in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the Private DNS zones within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Creates or updates a Private DNS zone. Does not modify Links to virtual networks or DNS records within the zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Deletes a Private DNS zone. WARNING: All DNS records in the zone will also be deleted. This operation cannot be undone. Private DNS zone cannot be deleted unless all virtual network links to it are removed. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="privateZoneName, resourceGroupName, subscriptionId" /> | Updates a Private DNS zone. Does not modify virtual network links or DNS records within the zone. |
