---
title: monitored_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_subscriptions
  - datadog
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitored_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.datadog.monitored_subscriptions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the monitored subscription resource. |
| <CopyableCode code="name" /> | `string` | Name of the monitored subscription resource. |
| <CopyableCode code="properties" /> | `object` | The request to update subscriptions needed to be monitored by the Datadog monitor resource. |
| <CopyableCode code="type" /> | `string` | The type of the monitored subscription resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="createor_update" /> | `EXEC` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="configurationName, monitorName, resourceGroupName, subscriptionId" /> |
