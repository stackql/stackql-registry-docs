---
title: dependency_map_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - dependency_map_controller
  - migrate
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
<tr><td><b>Name</b></td><td><code>dependency_map_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.dependency_map_controller" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="client_group_members" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | API to list client group members for the selected client group. |
| <CopyableCode code="export_dependencies" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | API to generate report containing agentless dependencies. |
| <CopyableCode code="generate_coarse_map" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | API to generate coarse map for the list of machines. |
| <CopyableCode code="generate_detailed_map" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | API to generate detailed map for a selected machine. |
| <CopyableCode code="server_group_members" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | API to list server group members for the selected server group. |
