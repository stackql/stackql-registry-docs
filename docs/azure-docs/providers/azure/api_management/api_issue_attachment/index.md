---
title: api_issue_attachment
hide_title: false
hide_table_of_contents: false
keywords:
  - api_issue_attachment
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
<tr><td><b>Name</b></td><td><code>api_issue_attachment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.api_issue_attachment" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Gets the details of the issue Attachment for an API specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="apiId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Lists all attachments for the Issue associated with the specified API. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Creates a new Attachment for the Issue in an API or updates an existing one. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, apiId, attachmentId, issueId, resourceGroupName, serviceName, subscriptionId" /> | Deletes the specified comment from an Issue. |
