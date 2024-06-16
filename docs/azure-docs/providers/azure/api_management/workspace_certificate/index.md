---
title: workspace_certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_certificate
  - api_management
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
<tr><td><b>Name</b></td><td><code>workspace_certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_certificate" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Gets the details of the certificate specified by its identifier. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists a collection of all certificates in the specified workspace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates or updates the certificate being used for authentication with the backend. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes specific certificate. |
| <CopyableCode code="refresh_secret" /> | `EXEC` | <CopyableCode code="certificateId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | From KeyVault, Refresh the certificate being used for authentication with the backend. |
