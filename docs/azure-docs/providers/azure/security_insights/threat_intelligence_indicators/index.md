---
title: threat_intelligence_indicators
hide_title: false
hide_table_of_contents: false
keywords:
  - threat_intelligence_indicators
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
<tr><td><b>Name</b></td><td><code>threat_intelligence_indicators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.threat_intelligence_indicators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of the threat intelligence entity |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ThreatIntelligenceIndicators_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
