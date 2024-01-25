---
title: replication_alert_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_alert_settings
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_alert_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_alert_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `location` | `string` | Resource Location |
| `properties` | `object` | The properties of an alert. |
| `type` | `string` | Resource Type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `alertSettingName, api-version, resourceGroupName, resourceName, subscriptionId` | Gets the details of the specified email notification(alert) configuration. |
| `list` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of email notification(alert) configurations for the vault. |
| `create` | `INSERT` | `alertSettingName, api-version, resourceGroupName, resourceName, subscriptionId` | Create or update an email notification(alert) configuration. |
| `_list` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of email notification(alert) configurations for the vault. |
