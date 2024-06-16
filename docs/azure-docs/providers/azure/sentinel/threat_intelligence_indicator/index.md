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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>threat_intelligence_indicator</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.threat_intelligence_indicator" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="kind" /> | `string` | The kind of the threat intelligence entity |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | View a threat intelligence indicator by name. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | Update a threat Intelligence indicator. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | Delete a threat intelligence indicator. |
| <CopyableCode code="append_tags" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | Append tags to a threat intelligence indicator. |
| <CopyableCode code="query_indicators" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Query threat intelligence indicators as per filtering criteria. |
| <CopyableCode code="replace_tags" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> | Replace tags added to a threat intelligence indicator. |
