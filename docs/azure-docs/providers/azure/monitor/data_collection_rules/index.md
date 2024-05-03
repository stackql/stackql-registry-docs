---
title: data_collection_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rules
  - monitor
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
<tr><td><b>Name</b></td><td><code>data_collection_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.data_collection_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | Resource entity tag (ETag). |
| <CopyableCode code="identity" /> | `object` | Managed service identity of the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives. |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataCollectionRuleName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataCollectionRuleName, resourceGroupName, subscriptionId, data__location" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataCollectionRuleName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dataCollectionRuleName, resourceGroupName, subscriptionId" /> |
