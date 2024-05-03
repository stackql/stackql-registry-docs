---
title: data_collection_rule_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rule_associations
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
<tr><td><b>Name</b></td><td><code>data_collection_rule_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.data_collection_rule_associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | Resource entity tag (ETag). |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="associationName, resourceUri" /> |
| <CopyableCode code="list_by_data_collection_endpoint" /> | `SELECT` | <CopyableCode code="dataCollectionEndpointName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list_by_resource" /> | `SELECT` | <CopyableCode code="resourceUri" /> |
| <CopyableCode code="list_by_rule" /> | `SELECT` | <CopyableCode code="dataCollectionRuleName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="associationName, resourceUri" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="associationName, resourceUri" /> |
| <CopyableCode code="_list_by_data_collection_endpoint" /> | `EXEC` | <CopyableCode code="dataCollectionEndpointName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list_by_resource" /> | `EXEC` | <CopyableCode code="resourceUri" /> |
| <CopyableCode code="_list_by_rule" /> | `EXEC` | <CopyableCode code="dataCollectionRuleName, resourceGroupName, subscriptionId" /> |
