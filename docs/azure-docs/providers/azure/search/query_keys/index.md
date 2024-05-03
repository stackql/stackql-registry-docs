---
title: query_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - query_keys
  - search
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
<tr><td><b>Name</b></td><td><code>query_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.search.query_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | Request URL that can be used to query next page of query keys. Returned when the total number of requested query keys exceed maximum page size. |
| <CopyableCode code="value" /> | `array` | The query keys for the search service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_search_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, searchServiceName, subscriptionId" /> | Returns the list of query API keys for the given search service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, searchServiceName, subscriptionId" /> | Generates a new query key for the specified search service. You can create up to 50 query keys per service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="key, resourceGroupName, searchServiceName, subscriptionId" /> | Deletes the specified query key. Unlike admin keys, query keys are not regenerated. The process for regenerating a query key is to delete and then recreate it. |
