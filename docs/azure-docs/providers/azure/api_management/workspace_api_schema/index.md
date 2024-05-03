---
title: workspace_api_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_schema
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
<tr><td><b>Name</b></td><td><code>workspace_api_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_schema" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, schemaId, serviceName, subscriptionId, workspaceId" /> | Get the schema configuration at the API level. |
| <CopyableCode code="list_by_api" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the schema configuration at the API level. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, resourceGroupName, schemaId, serviceName, subscriptionId, workspaceId" /> | Creates or updates schema configuration for the API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, resourceGroupName, schemaId, serviceName, subscriptionId, workspaceId" /> | Deletes the schema configuration at the Api. |
| <CopyableCode code="_list_by_api" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Get the schema configuration at the API level. |
