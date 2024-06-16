---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
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
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes incident properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a given incident. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets all incidents. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates an incident. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a given incident. |
| <CopyableCode code="run_playbook" /> | `EXEC` | <CopyableCode code="incidentIdentifier, resourceGroupName, subscriptionId, workspaceName, data__logicAppsResourceId" /> | Triggers playbook on a specific incident |
