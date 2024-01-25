---
title: job_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - job_credentials
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
<tr><td><b>Name</b></td><td><code>job_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_credentials</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a jobs credential. |
| `list_by_agent` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a list of jobs credentials. |
| `create_or_update` | `INSERT` | `credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId` | Creates or updates a job credential. |
| `delete` | `DELETE` | `credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId` | Deletes a job credential. |
| `_list_by_agent` | `EXEC` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a list of jobs credentials. |
