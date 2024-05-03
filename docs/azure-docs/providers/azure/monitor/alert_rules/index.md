---
title: alert_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rules
  - monitor
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
<tr><td><b>Name</b></td><td><code>alert_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.alert_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure resource Id |
| <CopyableCode code="name" /> | `string` | Azure resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | An alert rule. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Gets or sets a list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater in length than 128 characters and a value no greater in length than 256 characters. |
| <CopyableCode code="type" /> | `string` | Azure resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Gets a classic metric alert rule |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List the classic metric alert rules within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List the classic metric alert rules within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId, data__properties" /> | Creates or updates a classic metric alert rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Deletes a classic metric alert rule |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List the classic metric alert rules within a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List the classic metric alert rules within a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, ruleName, subscriptionId" /> | Updates an existing classic metric AlertRuleResource. To update other fields use the CreateOrUpdate method. |
