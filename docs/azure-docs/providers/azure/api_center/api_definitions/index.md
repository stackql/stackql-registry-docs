---
title: api_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - api_definitions
  - api_center
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
<tr><td><b>Name</b></td><td><code>api_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_center.api_definitions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Returns details of the API definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="apiName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Returns a collection of API definitions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Creates new or updates existing API definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Deletes specified API definition. |
| <CopyableCode code="export_specification" /> | `EXEC` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Exports the API specification. |
| <CopyableCode code="import_specification" /> | `EXEC` | <CopyableCode code="apiName, definitionName, resourceGroupName, serviceName, subscriptionId, versionName, workspaceName" /> | Imports the API specification. |
