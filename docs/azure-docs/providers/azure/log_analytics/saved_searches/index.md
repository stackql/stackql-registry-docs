---
title: saved_searches
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_searches
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>saved_searches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.saved_searches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the saved search. To override an existing saved search, use "*" or specify the current Etag |
| <CopyableCode code="properties" /> | `object` | Value object for saved search results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, savedSearchId, subscriptionId, workspaceName" /> | Gets the specified saved search for a given workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the saved searches for a given Log Analytics Workspace |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, savedSearchId, subscriptionId, workspaceName, data__properties" /> | Creates or updates a saved search for a given workspace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, savedSearchId, subscriptionId, workspaceName" /> | Deletes the specified saved search in a given workspace. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Gets the saved searches for a given Log Analytics Workspace |
