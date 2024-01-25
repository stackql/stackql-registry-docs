---
title: threat_intelligence_indicator
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intelligence_indicator
  - sentinel
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
<tr><td><b>Name</b></td><td><code>threat_intelligence_indicator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sentinel.threat_intelligence_indicator</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of the threat intelligence entity |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId, workspaceName` | View a threat intelligence indicator by name. |
| `create` | `INSERT` | `name, resourceGroupName, subscriptionId, workspaceName` | Update a threat Intelligence indicator. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId, workspaceName` | Delete a threat intelligence indicator. |
| `append_tags` | `EXEC` | `name, resourceGroupName, subscriptionId, workspaceName` | Append tags to a threat intelligence indicator. |
| `query_indicators` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Query threat intelligence indicators as per filtering criteria. |
| `replace_tags` | `EXEC` | `name, resourceGroupName, subscriptionId, workspaceName` | Replace tags added to a threat intelligence indicator. |
