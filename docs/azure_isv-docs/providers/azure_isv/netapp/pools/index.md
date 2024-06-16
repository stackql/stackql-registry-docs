---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - netapp
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
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Pool properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Get details of the specified capacity pool |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all capacity pools in the NetApp Account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create or Update a capacity pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Delete the specified capacity pool |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId" /> | Patch the specified capacity pool |
