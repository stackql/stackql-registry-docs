---
title: onboarding_states
hide_title: false
hide_table_of_contents: false
keywords:
  - onboarding_states
  - sentinel
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
<tr><td><b>Name</b></td><td><code>onboarding_states</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.onboarding_states" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | The Sentinel onboarding state properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName" /> | Get Sentinel onboarding state |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all Sentinel onboarding states |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName" /> | Create Sentinel onboarding state |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sentinelOnboardingStateName, subscriptionId, workspaceName" /> | Delete Sentinel onboarding state |
