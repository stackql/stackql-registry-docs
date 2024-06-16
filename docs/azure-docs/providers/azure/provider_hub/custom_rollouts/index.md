---
title: custom_rollouts
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_rollouts
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
<tr><td><b>Name</b></td><td><code>custom_rollouts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.provider_hub.custom_rollouts" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId" /> | Gets the custom rollout details. |
| <CopyableCode code="list_by_provider_registration" /> | `SELECT` | <CopyableCode code="providerNamespace, subscriptionId" /> | Gets the list of the custom rollouts for the given provider. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="providerNamespace, rolloutName, subscriptionId, data__properties" /> | Creates or updates the rollout details. |
