---
title: workspace_api_release
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_release
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
<tr><td><b>Name</b></td><td><code>workspace_api_release</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.workspace_api_release" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Returns the details of an API release. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Creates a new Release for the API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Deletes the specified release in the API. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="apiId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId, workspaceId" /> | Updates the details of the release of the API specified by its identifier. |
