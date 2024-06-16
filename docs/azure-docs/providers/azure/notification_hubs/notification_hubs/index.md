---
title: notification_hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_hubs
  - notification_hubs
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
<tr><td><b>Name</b></td><td><code>notification_hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.notification_hubs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | NotificationHub properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__location" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="check_notification_hub_availability" /> | `EXEC` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, data__name" /> |
| <CopyableCode code="debug_send" /> | `EXEC` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, namespaceName, notificationHubName, resourceGroupName, subscriptionId, data__policyKey" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |
