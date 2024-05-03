---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - device_update
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.device_update.private_link_resources" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, groupId, resourceGroupName, subscriptionId" /> | Get the specified private link resource associated with the device update account. |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all private link resources in a device update account. |
| <CopyableCode code="_list_by_account" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List all private link resources in a device update account. |
