---
title: incident_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_tasks
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
<tr><td><b>Name</b></td><td><code>incident_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incident_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an incident task |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentId, incidentTaskId, resourceGroupName, subscriptionId, workspaceName" /> | Gets an incident task. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all incident tasks. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentId, incidentTaskId, resourceGroupName, subscriptionId, workspaceName, data__properties" /> | Creates or updates the incident task. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentId, incidentTaskId, resourceGroupName, subscriptionId, workspaceName" /> | Delete the incident task. |
