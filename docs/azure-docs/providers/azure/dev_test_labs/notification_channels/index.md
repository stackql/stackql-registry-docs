---
title: notification_channels
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_channels
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>notification_channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.notification_channels" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a schedule. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Get notification channel. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, labName, resourceGroupName, subscriptionId" /> | List notification channels in a given lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId, data__properties" /> | Create or replace an existing notification channel. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Delete notification channel. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="api-version, labName, resourceGroupName, subscriptionId" /> | List notification channels in a given lab. |
| <CopyableCode code="notify" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Send notification to provided channel. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, labName, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of notification channels. All other properties will be ignored. |
