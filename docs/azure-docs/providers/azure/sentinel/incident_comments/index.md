---
title: incident_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_comments
  - sentinel
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
<tr><td><b>Name</b></td><td><code>incident_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sentinel.incident_comments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Etag of the azure resource |
| <CopyableCode code="properties" /> | `object` | Incident comment property bag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets a comment for a given incident. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Gets all comments for a given incident. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Creates or updates a comment for a given incident. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="incidentCommentId, incidentId, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a comment for a given incident. |
