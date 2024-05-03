---
title: web_apps_triggered_web_job_history_slot
hide_title: false
hide_table_of_contents: false
keywords:
  - web_apps_triggered_web_job_history_slot
  - app_service
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
<tr><td><b>Name</b></td><td><code>web_apps_triggered_web_job_history_slot</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.web_apps_triggered_web_job_history_slot" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | TriggeredJobHistory resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, name, resourceGroupName, slot, subscriptionId, webJobName" /> | Description for Gets a triggered web job's history by its ID for an app, , or a deployment slot. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, webJobName" /> | Description for List a triggered web job's history for an app, or a deployment slot. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId, webJobName" /> | Description for List a triggered web job's history for an app, or a deployment slot. |
