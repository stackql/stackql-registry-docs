---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
  - traffic_manager
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
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.traffic_manager.profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The Azure Region where the resource lives |
| <CopyableCode code="properties" /> | `object` | Class representing the Traffic Manager profile properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Gets a Traffic Manager profile. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Traffic Manager profiles within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all Traffic Manager profiles within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Create or update a Traffic Manager profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Deletes a Traffic Manager profile. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Traffic Manager profiles within a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all Traffic Manager profiles within a subscription. |
| <CopyableCode code="check_traffic_manager_name_availability_v2" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Checks the availability of a Traffic Manager Relative DNS name. |
| <CopyableCode code="check_traffic_manager_relative_dns_name_availability" /> | `EXEC` |  | Checks the availability of a Traffic Manager Relative DNS name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> | Update a Traffic Manager profile. |
