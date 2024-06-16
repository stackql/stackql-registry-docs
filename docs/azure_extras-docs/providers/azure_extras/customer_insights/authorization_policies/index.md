---
title: authorization_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_policies
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>authorization_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.authorization_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | The authorization policy. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Gets an authorization policy in the hub. |
| <CopyableCode code="list_by_hub" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets all the authorization policies in a specified hub. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Creates an authorization policy or updates an existing authorization policy. |
| <CopyableCode code="regenerate_primary_key" /> | `EXEC` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Regenerates the primary policy key of the specified authorization policy. |
| <CopyableCode code="regenerate_secondary_key" /> | `EXEC` | <CopyableCode code="authorizationPolicyName, hubName, resourceGroupName, subscriptionId" /> | Regenerates the secondary policy key of the specified authorization policy. |
