---
title: sign_up_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - sign_up_settings
  - api_management
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
<tr><td><b>Name</b></td><td><code>sign_up_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.sign_up_settings</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Get Sign Up Settings for the Portal |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId` | Create or Update Sign-Up settings. |
| `update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId` | Update Sign-Up settings. |
