---
title: managed_database_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_security_alert_policies
  - sql
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
<tr><td><b>Name</b></td><td><code>managed_database_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_security_alert_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabaseSecurityAlertPolicies_Get` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, securityAlertPolicyName, subscriptionId` | Gets a managed database's security alert policy. |
| `ManagedDatabaseSecurityAlertPolicies_ListByDatabase` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a list of managed database's security alert policies. |
| `ManagedDatabaseSecurityAlertPolicies_CreateOrUpdate` | `INSERT` | `databaseName, managedInstanceName, resourceGroupName, securityAlertPolicyName, subscriptionId` | Creates or updates a database's security alert policy. |
