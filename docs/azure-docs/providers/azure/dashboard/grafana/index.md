---
title: grafana
hide_title: false
hide_table_of_contents: false
keywords:
  - grafana
  - dashboard
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
<tr><td><b>Name</b></td><td><code>grafana</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dashboard.grafana" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ARM id of the grafana resource |
| <CopyableCode code="name" /> | `string` | Name of the grafana resource. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the grafana resource lives |
| <CopyableCode code="properties" /> | `object` | Properties specific to the grafana resource. |
| <CopyableCode code="sku" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The tags for grafana resource. |
| <CopyableCode code="type" /> | `string` | The type of the grafana resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="check_enterprise_details" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="fetch_available_plugins" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |
