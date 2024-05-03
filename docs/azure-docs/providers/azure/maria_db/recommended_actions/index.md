---
title: recommended_actions
hide_title: false
hide_table_of_contents: false
keywords:
  - recommended_actions
  - maria_db
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
<tr><td><b>Name</b></td><td><code>recommended_actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maria_db.recommended_actions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="advisorName, recommendedActionName, resourceGroupName, serverName, subscriptionId" /> |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="advisorName, resourceGroupName, serverName, subscriptionId" /> |
| <CopyableCode code="_list_by_server" /> | `EXEC` | <CopyableCode code="advisorName, resourceGroupName, serverName, subscriptionId" /> |
