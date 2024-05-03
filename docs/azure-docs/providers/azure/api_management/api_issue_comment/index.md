---
title: api_issue_comment
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue_comment
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
<tr><td><b>Name</b></td><td><code>api_issue_comment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_issue_comment" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the issue Comment for an API specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Lists all comments for the Issue associated with the specified API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Comment for the Issue in an API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, commentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified comment from an Issue. |
| <CopyableCode code="_list_by_service" /> | `EXEC` | <CopyableCode code="apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Lists all comments for the Issue associated with the specified API. |
