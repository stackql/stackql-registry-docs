---
title: recovery_points_recommended_for_move
hide_title: false
hide_table_of_contents: false
keywords:
  - recovery_points_recommended_for_move
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>recovery_points_recommended_for_move</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_backup.recovery_points_recommended_for_move" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | The uri to fetch the next page of resources. Call ListNext() fetches next page of resources. |
| <CopyableCode code="value" /> | `array` | List of resources. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, containerName, fabricName, protectedItemName, resourceGroupName, subscriptionId, vaultName" /> |
