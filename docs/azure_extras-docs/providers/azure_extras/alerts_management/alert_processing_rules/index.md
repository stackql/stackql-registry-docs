---
title: alert_processing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_processing_rules
  - alerts_management
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.alerts_management.alert_processing_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Alert processing rule properties defining scopes, conditions and scheduling logic for alert processing rule. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AlertProcessingRules_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List all alert processing rules in a resource group. |
| `AlertProcessingRules_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | List all alert processing rules in a subscription. |
| `AlertProcessingRules_CreateOrUpdate` | `INSERT` | `alertProcessingRuleName, api-version, resourceGroupName, subscriptionId` | Create or update an alert processing rule. |
| `AlertProcessingRules_Delete` | `DELETE` | `alertProcessingRuleName, api-version, resourceGroupName, subscriptionId` | Delete an alert processing rule. |
| `AlertProcessingRules_GetByName` | `EXEC` | `alertProcessingRuleName, api-version, resourceGroupName, subscriptionId` | Get an alert processing rule by name. |
| `AlertProcessingRules_Update` | `EXEC` | `alertProcessingRuleName, api-version, resourceGroupName, subscriptionId` | Enable, disable, or update tags for an alert processing rule. |
