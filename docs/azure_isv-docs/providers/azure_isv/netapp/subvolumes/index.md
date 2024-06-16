---
title: subvolumes
hide_title: false
hide_table_of_contents: false
keywords:
  - subvolumes
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
<tr><td><b>Name</b></td><td><code>subvolumes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.netapp.subvolumes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Returns the path associated with the subvolumeName provided |
| <CopyableCode code="list_by_volume" /> | `SELECT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, volumeName" /> | Returns a list of the subvolumes in the volume |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Creates a subvolume in the path or clones the subvolume mentioned in the parentPath |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Delete subvolume |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, poolName, resourceGroupName, subscriptionId, subvolumeName, volumeName" /> | Patch a subvolume |
