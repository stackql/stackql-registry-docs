---
title: runs_log_sas_url
hide_title: false
hide_table_of_contents: false
keywords:
  - runs_log_sas_url
  - container_registry
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
<tr><td><b>Name</b></td><td><code>runs_log_sas_url</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.runs_log_sas_url</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `logArtifactLink` | `string` | The link to logs in registry for a run on a azure container registry. |
| `logLink` | `string` | The link to logs for a run on a azure container registry. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `registryName, resourceGroupName, runId, subscriptionId` |
