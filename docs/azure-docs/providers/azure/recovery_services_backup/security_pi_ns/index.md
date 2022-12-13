---
title: security_pi_ns
hide_title: false
hide_table_of_contents: false
keywords:
  - security_pi_ns
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>security_pi_ns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.security_pi_ns</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `token` | `string` | Token value. |
| `expiryTimeInUtcTicks` | `integer` | Expiry time of token. |
| `securityPIN` | `string` | Security PIN |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SecurityPINs_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` |
