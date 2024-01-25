---
title: available_inplace_upgrade_os
hide_title: false
hide_table_of_contents: false
keywords:
  - available_inplace_upgrade_os
  - test_base
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_inplace_upgrade_os</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.available_inplace_upgrade_os</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `availableInplaceUpgradeOSResourceName, resourceGroupName, subscriptionId, testBaseAccountName` | Gets an available In-place Upgrade OS to run a package under a Test Base Account. |
| `list` | `SELECT` | `osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the available In-place Upgrade OSs to a package under a Test Base Account. |
| `_list` | `EXEC` | `osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the available In-place Upgrade OSs to a package under a Test Base Account. |
