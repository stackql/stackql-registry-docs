---
title: updates
hide_title: false
hide_table_of_contents: false
keywords:
  - updates
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.updates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of a singular Update in HCI Cluster |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Get specified Update |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List all Updates |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Delete specified Update |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | List all Updates |
| <CopyableCode code="post" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Apply Update |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | Put specified Update |
