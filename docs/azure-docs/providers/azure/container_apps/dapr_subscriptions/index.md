---
title: dapr_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - dapr_subscriptions
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
<tr><td><b>Name</b></td><td><code>dapr_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.dapr_subscriptions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Creates or updates a Dapr subscription in a Managed Environment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, name, resourceGroupName, subscriptionId" /> | Delete a Dapr subscription from a Managed Environment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> |  |
