---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.alerts_management.alerts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Alerts_ChangeState` | `EXEC` | `alertId, api-version, newState, subscriptionId` | Change the state of an alert. |
| `Alerts_GetAll` | `EXEC` | `api-version, subscriptionId` | List all existing alerts, where the results can be filtered on the basis of multiple parameters (e.g. time range). The results can then be sorted on the basis specific fields, with the default being lastModifiedDateTime.  |
| `Alerts_GetById` | `EXEC` | `alertId, api-version, subscriptionId` | Get information related to a specific alert |
| `Alerts_GetHistory` | `EXEC` | `alertId, api-version, subscriptionId` | Get the history of an alert, which captures any monitor condition changes (Fired/Resolved) and alert state changes (New/Acknowledged/Closed). |
| `Alerts_GetSummary` | `EXEC` | `api-version, groupby, subscriptionId` | Get a summarized count of your alerts grouped by various parameters (e.g. grouping by 'Severity' returns the count of alerts for each severity). |
| `Alerts_MetaData` | `EXEC` | `api-version, identifier` | List alerts meta data information based on value of identifier parameter. |
