---
title: policy_restriction
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_restriction
  - api_management
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
<tr><td><b>Name</b></td><td><code>policy_restriction</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.policy_restriction" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Get the policy restriction of the Api Management service. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Gets all policy restrictions of API Management services. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates the policy restriction configuration of the Api Management service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the policy restriction configuration of the Api Management Service. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, policyRestrictionId, resourceGroupName, serviceName, subscriptionId" /> | Updates the policy restriction configuration of the Api Management service. |
