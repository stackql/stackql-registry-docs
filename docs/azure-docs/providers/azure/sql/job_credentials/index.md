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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobCredentials_Get` | `SELECT` | `credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a jobs credential. |
| `JobCredentials_ListByAgent` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a list of jobs credentials. |
| `JobCredentials_CreateOrUpdate` | `INSERT` | `credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId` | Creates or updates a job credential. |
| `JobCredentials_Delete` | `DELETE` | `credentialName, jobAgentName, resourceGroupName, serverName, subscriptionId` | Deletes a job credential. |
