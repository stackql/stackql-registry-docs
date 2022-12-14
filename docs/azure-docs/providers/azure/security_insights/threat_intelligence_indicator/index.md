---
title: threat_intelligence_indicator
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intelligence_indicator
  - security_insights
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
<tr><td><b>Id</b></td><td><code>azure.security_insights.threat_intelligence_indicator</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The kind of the threat intelligence entity |
| `etag` | `string` | Etag of the azure resource |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ThreatIntelligenceIndicator_Get` | `SELECT` | `name, resourceGroupName, subscriptionId, workspaceName` | View a threat intelligence indicator by name. |
| `ThreatIntelligenceIndicator_Create` | `INSERT` | `name, resourceGroupName, subscriptionId, workspaceName` | Update a threat Intelligence indicator. |
| `ThreatIntelligenceIndicator_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId, workspaceName` | Delete a threat intelligence indicator. |
| `ThreatIntelligenceIndicator_AppendTags` | `EXEC` | `name, resourceGroupName, subscriptionId, workspaceName` | Append tags to a threat intelligence indicator. |
| `ThreatIntelligenceIndicator_CreateIndicator` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Create a new threat intelligence indicator. |
| `ThreatIntelligenceIndicator_QueryIndicators` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Query threat intelligence indicators as per filtering criteria. |
| `ThreatIntelligenceIndicator_ReplaceTags` | `EXEC` | `name, resourceGroupName, subscriptionId, workspaceName` | Replace tags added to a threat intelligence indicator. |
