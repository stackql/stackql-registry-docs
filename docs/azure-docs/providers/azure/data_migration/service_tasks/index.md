---
title: service_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - service_tasks
  - data_migration
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
<tr><td><b>Name</b></td><td><code>service_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_migration.service_tasks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | HTTP strong entity tag value. This is ignored if submitted. |
| <CopyableCode code="properties" /> | `object` | Base class for all types of DMS (classic) task properties. If task is not supported by current client, this object is returned. |
| <CopyableCode code="systemData" /> | `object` |  |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` |  | The service tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The GET method retrieves information about a service task. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId" /> | The services resource is the top-level resource that represents the Azure Database Migration Service (classic). This method returns a list of service level tasks owned by a service resource. Some tasks may have a status of Unknown, which indicates that an error occurred while querying the status of that task. |
| <CopyableCode code="create_or_update" /> | `INSERT` |  | The service tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PUT method creates a new service task or updates an existing one, although since service tasks have no mutable custom properties, there is little reason to update an existing one. |
| <CopyableCode code="delete" /> | `DELETE` |  | The service tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The DELETE method deletes a service task, canceling it first if it's running. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="api-version, groupName, serviceName, subscriptionId, taskName" /> | The service tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. This method cancels a service task if it's currently queued or running. |
| <CopyableCode code="update" /> | `EXEC` |  | The service tasks resource is a nested, proxy-only resource representing work performed by a DMS (classic) instance. The PATCH method updates an existing service task, but since service tasks have no mutable custom properties, there is little reason to do so. |
