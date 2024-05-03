---
title: rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - rollouts
  - deployment_manager
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
<tr><td><b>Name</b></td><td><code>rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.deployment_manager.rollouts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties that define a rollout. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, rolloutName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, rolloutName, subscriptionId, data__identity, data__properties" /> | This is an asynchronous operation and can be polled to completion using the location header returned by this operation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, rolloutName, subscriptionId" /> | Only rollouts in terminal state can be deleted. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="resourceGroupName, rolloutName, subscriptionId" /> | Only running rollouts can be canceled. |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="resourceGroupName, rolloutName, subscriptionId" /> | Only failed rollouts can be restarted. |
