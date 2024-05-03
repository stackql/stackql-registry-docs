---
title: mongo_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_clusters
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>mongo_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.mongo_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a mongo cluster. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Gets information about a mongo cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the mongo clusters in a given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the mongo clusters in a given resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Create or update a mongo cluster. Update overwrites all properties for the resource. To only modify some of the properties, use PATCH. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Deletes a mongo cluster. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all the mongo clusters in a given subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the mongo clusters in a given resource group. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Check the availability of name for resource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="mongoClusterName, resourceGroupName, subscriptionId" /> | Updates an existing mongo cluster. The request body can contain one to many of the properties present in the normal mongo cluster definition. |
