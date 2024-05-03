---
title: portal_config
hide_title: false
hide_table_of_contents: false
keywords:
  - portal_config
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
<tr><td><b>Name</b></td><td><code>portal_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.portal_config" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="portalConfigId, resourceGroupName, serviceName, subscriptionId" /> | Get the developer portal configuration. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists the developer portal configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="If-Match, portalConfigId, resourceGroupName, serviceName, subscriptionId" /> | Create or update the developer portal configuration. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists the developer portal configurations. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, portalConfigId, resourceGroupName, serviceName, subscriptionId" /> | Update the developer portal configuration. |
