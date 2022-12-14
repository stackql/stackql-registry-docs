---
title: managed_server_security_alert_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_server_security_alert_policies
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
<tr><td><b>Name</b></td><td><code>managed_server_security_alert_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_server_security_alert_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a security alert policy. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedServerSecurityAlertPolicies_Get` | `SELECT` | `managedInstanceName, resourceGroupName, securityAlertPolicyName, subscriptionId` | Get a managed server's threat detection policy. |
| `ManagedServerSecurityAlertPolicies_ListByInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Get the managed server's threat detection policies. |
| `ManagedServerSecurityAlertPolicies_CreateOrUpdate` | `INSERT` | `managedInstanceName, resourceGroupName, securityAlertPolicyName, subscriptionId` | Creates or updates a threat detection policy. |
