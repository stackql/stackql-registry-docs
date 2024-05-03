---
title: triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - triggers
  - data_factory
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
<tr><td><b>Name</b></td><td><code>triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.triggers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | Azure data factory nested object which contains information about creating pipeline run |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, triggerName" /> | Gets a trigger. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Lists triggers. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, triggerName, data__properties" /> | Creates or updates a trigger. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, triggerName" /> | Deletes a trigger. |
| <CopyableCode code="_list_by_factory" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Lists triggers. |
| <CopyableCode code="query_by_factory" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId" /> | Query triggers. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, triggerName" /> | Starts a trigger. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, triggerName" /> | Stops a trigger. |
| <CopyableCode code="subscribe_to_events" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, triggerName" /> | Subscribe event trigger to events. |
| <CopyableCode code="unsubscribe_from_events" /> | `EXEC` | <CopyableCode code="api-version, factoryName, resourceGroupName, subscriptionId, triggerName" /> | Unsubscribe event trigger from events. |
