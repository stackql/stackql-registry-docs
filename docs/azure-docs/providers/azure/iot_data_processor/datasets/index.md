---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
  - iot_data_processor
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
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_data_processor.datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | Extended location is an extension of Azure locations. They provide a way to use their Azure ARC enabled Kubernetes clusters as target locations for deploying Azure services instances. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | The properties of a Dataset resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId" /> | Get a Dataset |
| <CopyableCode code="list_by_instance" /> | `SELECT` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | List Dataset resources by Instance |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a Dataset |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId" /> | Delete a Dataset |
| <CopyableCode code="_list_by_instance" /> | `EXEC` | <CopyableCode code="instanceName, resourceGroupName, subscriptionId" /> | List Dataset resources by Instance |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="datasetName, instanceName, resourceGroupName, subscriptionId" /> | Update a Dataset |
