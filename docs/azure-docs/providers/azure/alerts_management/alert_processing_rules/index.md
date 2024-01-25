---
title: alert_processing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_processing_rules
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
<tr><td><b>Name</b></td><td><code>alert_processing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.alerts_management.alert_processing_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location |
| `properties` | `object` | Alert processing rule properties defining scopes, conditions and scheduling logic for alert processing rule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all alert processing rules in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all alert processing rules in a subscription. |
| `create_or_update` | `INSERT` | `alertProcessingRuleName, resourceGroupName, subscriptionId` | Create or update an alert processing rule. |
| `delete` | `DELETE` | `alertProcessingRuleName, resourceGroupName, subscriptionId` | Delete an alert processing rule. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all alert processing rules in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all alert processing rules in a subscription. |
| `get_by_name` | `EXEC` | `alertProcessingRuleName, resourceGroupName, subscriptionId` | Get an alert processing rule by name. |
| `update` | `EXEC` | `alertProcessingRuleName, resourceGroupName, subscriptionId` | Enable, disable, or update tags for an alert processing rule. |
