---
title: container_apps
hide_title: false
hide_table_of_contents: false
keywords:
  - container_apps
  - container_apps
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
<tr><td><b>Name</b></td><td><code>container_apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.container_apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="managedBy" /> | `string` | The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource. |
| <CopyableCode code="properties" /> | `object` | ContainerApp resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> | Create or update a Container App. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> | Delete a Container App. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="containerAppName, resourceGroupName, subscriptionId" /> | Patches a Container App using JSON Merge Patch |
