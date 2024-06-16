---
title: route_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - route_policies
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>route_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.route_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | RoutePolicyProperties defines the resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Implements Route Policy GET method. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Implements RoutePolicies list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Implements RoutePolicies list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId, data__location, data__properties" /> | Implements Route Policy PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Implements Route Policy DELETE method. |
| <CopyableCode code="commit_configuration" /> | `EXEC` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Commits the configuration of the given resources. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | API to update certain properties of the Route Policy resource. |
| <CopyableCode code="validate_configuration" /> | `EXEC` | <CopyableCode code="resourceGroupName, routePolicyName, subscriptionId" /> | Validates the configuration of the resources. |
