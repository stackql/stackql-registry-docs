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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>available_inplace_upgrade_os</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.available_inplace_upgrade_os" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availableInplaceUpgradeOSResourceName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Gets an available In-place Upgrade OS to run a package under a Test Base Account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the available In-place Upgrade OSs to a package under a Test Base Account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="osUpdateType, resourceGroupName, subscriptionId, testBaseAccountName" /> | Lists all the available In-place Upgrade OSs to a package under a Test Base Account. |
