---
title: prometheus_rule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - prometheus_rule_groups
  - alerts_management
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>prometheus_rule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.alerts_management.prometheus_rule_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | An Azure Prometheus rule group. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, ruleGroupName, subscriptionId` | Retrieve a Prometheus rule group definition. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieve Prometheus rule group definitions in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieve Prometheus all rule group definitions in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, ruleGroupName, subscriptionId, data__properties` | Create or update a Prometheus rule group definition. |
| `delete` | `DELETE` | `resourceGroupName, ruleGroupName, subscriptionId` | Delete a Prometheus rule group definition. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieve Prometheus rule group definitions in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieve Prometheus all rule group definitions in a subscription. |
| `update` | `EXEC` | `resourceGroupName, ruleGroupName, subscriptionId` | Update an Prometheus rule group definition. |
