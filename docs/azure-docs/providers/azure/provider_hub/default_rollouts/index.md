---
title: default_rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - default_rollouts
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>default_rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.default_rollouts" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Gets the default rollout details. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the rollouts for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Creates or updates the rollout details. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Deletes the rollout resource. Rollout must be in terminal state. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Stops or cancels the rollout, if in progress. |
