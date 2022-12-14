---
title: workspace_purge
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_purge
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>workspace_purge</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.workspace_purge</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspacePurge_GetPurgeStatus` | `EXEC` | `purgeId, resourceGroupName, subscriptionId, workspaceName` | Gets status of an ongoing purge operation. |
| `WorkspacePurge_Purge` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName, data__filters, data__table` | Purges data in an Log Analytics workspace by a set of user-defined filters.<br /><br />In order to manage system resources, purge requests are throttled at 50 requests per hour. You should batch the execution of purge requests by sending a single command whose predicate includes all user identities that require purging. Use the in operator to specify multiple identities. You should run the query prior to using for a purge request to verify that the results are expected.<br />Log Analytics only supports purge operations required for compliance with GDPR. The Log Analytics product team reserves the right to reject requests for purge operations that are not for the purpose of GDPR compliance. In the event of a dispute, please create a support ticket |
