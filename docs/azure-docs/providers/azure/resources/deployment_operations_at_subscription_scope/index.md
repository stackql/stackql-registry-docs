---
title: deployment_operations_at_subscription_scope
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_operations_at_subscription_scope
  - resources
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
<tr><td><b>Name</b></td><td><code>deployment_operations_at_subscription_scope</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.deployment_operations_at_subscription_scope" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Full deployment operation ID. |
| <CopyableCode code="operationId" /> | `string` | Deployment operation ID. |
| <CopyableCode code="properties" /> | `object` | Deployment operation properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="deploymentName, operationId, subscriptionId" /> | Gets a deployments operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentName, subscriptionId" /> | Gets all deployments operations for a deployment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="deploymentName, subscriptionId" /> | Gets all deployments operations for a deployment. |
