---
title: data_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - data_sources
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
<tr><td><b>Name</b></td><td><code>data_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.log_analytics.data_sources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | The ETag of the data source. |
| <CopyableCode code="kind" /> | `string` | The kind of the DataSource. |
| <CopyableCode code="properties" /> | `object` | JSON object |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataSourceName, resourceGroupName, subscriptionId, workspaceName" /> | Gets a datasource instance. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="$filter, resourceGroupName, subscriptionId, workspaceName" /> | Gets the first page of data source instances in a workspace with the link to the next page. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataSourceName, resourceGroupName, subscriptionId, workspaceName, data__kind, data__properties" /> | Create or update a data source. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataSourceName, resourceGroupName, subscriptionId, workspaceName" /> | Deletes a data source instance. |
| <CopyableCode code="_list_by_workspace" /> | `EXEC` | <CopyableCode code="$filter, resourceGroupName, subscriptionId, workspaceName" /> | Gets the first page of data source instances in a workspace with the link to the next page. |
