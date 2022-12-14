---
title: trigger_runs
hide_title: false
hide_table_of_contents: false
keywords:
  - trigger_runs
  - data_factory
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
<tr><td><b>Name</b></td><td><code>trigger_runs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.trigger_runs</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TriggerRuns_Cancel` | `EXEC` | `api-version, factoryName, resourceGroupName, runId, subscriptionId, triggerName` | Cancel a single trigger instance by runId. |
| `TriggerRuns_QueryByFactory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId, data__lastUpdatedAfter, data__lastUpdatedBefore` | Query trigger runs. |
| `TriggerRuns_Rerun` | `EXEC` | `api-version, factoryName, resourceGroupName, runId, subscriptionId, triggerName` | Rerun single trigger instance by runId. |
