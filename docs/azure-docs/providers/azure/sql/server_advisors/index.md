---
title: server_advisors
hide_title: false
hide_table_of_contents: false
keywords:
  - server_advisors
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
<tr><td><b>Name</b></td><td><code>server_advisors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_advisors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties for a Database, Server or Elastic Pool Advisor. |
| `kind` | `string` | Resource kind. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerAdvisors_Get` | `SELECT` | `advisorName, resourceGroupName, serverName, subscriptionId` | Gets a server advisor. |
| `ServerAdvisors_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server advisors. |
| `ServerAdvisors_Update` | `EXEC` | `advisorName, resourceGroupName, serverName, subscriptionId` | Updates a server advisor. |
