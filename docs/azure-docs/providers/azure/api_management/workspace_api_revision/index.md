---
title: workspace_api_revision
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_revision
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
<tr><td><b>Name</b></td><td><code>workspace_api_revision</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_revision" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | Description of the API Revision. |
| <CopyableCode code="apiId" /> | `string` | Identifier of the API Revision. |
| <CopyableCode code="apiRevision" /> | `string` | Revision number of API. |
| <CopyableCode code="createdDateTime" /> | `string` | The time the API Revision was created. The date conforms to the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard. |
| <CopyableCode code="isCurrent" /> | `boolean` | Indicates if API revision is accessible via the gateway. |
| <CopyableCode code="isOnline" /> | `boolean` | Indicates if API revision is the current api revision. |
| <CopyableCode code="privateUrl" /> | `string` | Gateway URL for accessing the non-current API Revision. |
| <CopyableCode code="updatedDateTime" /> | `string` | The time the API Revision were updated. The date conforms to the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> |
