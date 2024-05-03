---
title: policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policy
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
<tr><td><b>Name</b></td><td><code>policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.policy" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyId, resourceGroupName, serviceName, subscriptionId" /> | Get the Global policy definition of the Api Management service. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all the Global Policy definitions of the Api Management service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="policyId, resourceGroupName, serviceName, subscriptionId" /> | Creates or updates the global policy configuration of the Api Management service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, policyId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the global policy configuration of the Api Management Service. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists all the Global Policy definitions of the Api Management service. |
