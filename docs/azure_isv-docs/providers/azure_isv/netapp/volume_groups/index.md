---
title: volume_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_groups
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
<tr><td><b>Name</b></td><td><code>volume_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.volume_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Volume group properties |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, volumeGroupName" /> | Get details of the specified volume group |
| <CopyableCode code="list_by_netapp_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all volume groups for given account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, volumeGroupName" /> | Create a volume group along with specified volumes |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, volumeGroupName" /> | Delete the specified volume group only if there are no volumes under volume group. |
| <CopyableCode code="_list_by_netapp_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all volume groups for given account |
