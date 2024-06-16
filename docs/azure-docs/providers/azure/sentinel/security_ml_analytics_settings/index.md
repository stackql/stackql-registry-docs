---
title: security_ml_analytics_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - security_ml_analytics_settings
  - sentinel
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
<tr><td><b>Name</b></td><td><code>security_ml_analytics_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.security_ml_analytics_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="kind" /> | `string` | The kind of security ML analytics settings |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, settingsResourceName, subscriptionId, workspaceName" /> | Gets the Security ML Analytics Settings. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all Security ML Analytics Settings. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, settingsResourceName, subscriptionId, workspaceName, data__kind" /> | Creates or updates the Security ML Analytics Settings. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, settingsResourceName, subscriptionId, workspaceName" /> | Delete the Security ML Analytics Settings. |
