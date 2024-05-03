---
title: connected_environments_dapr_components
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_dapr_components
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
<tr><td><b>Name</b></td><td><code>connected_environments_dapr_components</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments_dapr_components" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="componentName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="componentName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Creates or updates a Dapr Component in a connected environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="componentName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Delete a Dapr Component from a connected environment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
