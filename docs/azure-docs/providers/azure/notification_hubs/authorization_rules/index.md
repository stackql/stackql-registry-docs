---
title: authorization_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - authorization_rules
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
<tr><td><b>Name</b></td><td><code>authorization_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.notification_hubs.authorization_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Deprecated - only for compatibility. |
| <CopyableCode code="properties" /> | `object` | SharedAccessAuthorizationRule properties. |
| <CopyableCode code="tags" /> | `object` | Deprecated - only for compatibility. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="namespaceName, notificationHubName, resourceGroupName, subscriptionId" /> |
