---
title: dapr_component_resiliency_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - dapr_component_resiliency_policies
  - container_apps
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
<tr><td><b>Name</b></td><td><code>dapr_component_resiliency_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.dapr_component_resiliency_policies" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="componentName, environmentName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="componentName, environmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="componentName, environmentName, name, resourceGroupName, subscriptionId" /> | Creates or updates a resiliency policy for a Dapr component. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="componentName, environmentName, name, resourceGroupName, subscriptionId" /> | Delete a resiliency policy for a Dapr component. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="componentName, environmentName, resourceGroupName, subscriptionId" /> |  |
