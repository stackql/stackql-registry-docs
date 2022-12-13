---
title: alert_rule_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - alert_rule_incidents
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alert_rule_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.alert_rule_incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Incident name. |
| `activatedTime` | `string` | The time at which the incident was activated in ISO8601 format. |
| `isActive` | `boolean` | A boolean to indicate whether the incident is active or resolved. |
| `resolvedTime` | `string` | The time at which the incident was resolved in ISO8601 format. If null, it means the incident is still active. |
| `ruleName` | `string` | Rule name that is associated with the incident. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AlertRuleIncidents_Get` | `SELECT` | `incidentName, resourceGroupName, ruleName, subscriptionId` | Gets an incident associated to an alert rule |
| `AlertRuleIncidents_ListByAlertRule` | `SELECT` | `resourceGroupName, ruleName, subscriptionId` | Gets a list of incidents associated to an alert rule |
