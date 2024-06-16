---
title: update_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - update_runs
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
<tr><td><b>Name</b></td><td><code>update_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.azure_stack_hci.update_runs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Details of an Update run |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName, updateRunName" /> | Get the Update run for a specified update |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName" /> | List all Update runs for a specified update |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName, updateRunName" /> | Delete specified Update Run |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, updateName, updateRunName" /> | Put Update runs for a specified update |
