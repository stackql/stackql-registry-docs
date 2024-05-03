---
title: resource_health_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_health_metadata
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
<tr><td><b>Name</b></td><td><code>resource_health_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.resource_health_metadata" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | ResourceHealthMetadata resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Description for List all ResourceHealthMetadata for all sites in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription. |
| <CopyableCode code="list_by_site" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| <CopyableCode code="list_by_site_slot" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Description for List all ResourceHealthMetadata for all sites in the subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Description for List all ResourceHealthMetadata for all sites in the resource group in the subscription. |
| <CopyableCode code="_list_by_site" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| <CopyableCode code="_list_by_site_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the category of ResourceHealthMetadata to use for the given site as a collection |
| <CopyableCode code="get_by_site" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets the category of ResourceHealthMetadata to use for the given site |
| <CopyableCode code="get_by_site_slot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, slot, subscriptionId" /> | Description for Gets the category of ResourceHealthMetadata to use for the given site |
