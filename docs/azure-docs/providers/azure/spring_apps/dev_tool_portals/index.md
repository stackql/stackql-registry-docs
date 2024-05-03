---
title: dev_tool_portals
hide_title: false
hide_table_of_contents: false
keywords:
  - dev_tool_portals
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>dev_tool_portals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.dev_tool_portals" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devToolPortalName, resourceGroupName, serviceName, subscriptionId" /> | Get the Application Live  and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devToolPortalName, resourceGroupName, serviceName, subscriptionId" /> | Create the default Dev Tool Portal or update the existing Dev Tool Portal. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devToolPortalName, resourceGroupName, serviceName, subscriptionId" /> | Disable the default Dev Tool Portal. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in a Service. |
