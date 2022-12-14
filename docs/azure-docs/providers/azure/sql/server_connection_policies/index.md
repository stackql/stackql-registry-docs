---
title: server_connection_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - server_connection_policies
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
<tr><td><b>Name</b></td><td><code>server_connection_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_connection_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Metadata used for the Azure portal experience. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The properties of a server connection policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerConnectionPolicies_Get` | `SELECT` | `connectionPolicyName, resourceGroupName, serverName, subscriptionId` | Gets a server connection policy |
| `ServerConnectionPolicies_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists connection policy |
| `ServerConnectionPolicies_CreateOrUpdate` | `INSERT` | `connectionPolicyName, resourceGroupName, serverName, subscriptionId` | Updates a server connection policy |
