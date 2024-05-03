---
title: open_shift_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - open_shift_clusters
  - redhat_openshift
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>open_shift_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redhat_openshift.open_shift_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | OpenShiftClusterProperties represents an OpenShift cluster's properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a OpenShift cluster. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The operation returns properties of each OpenShift cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The operation returns properties of each OpenShift cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a OpenShift cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns nothing. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The operation returns properties of each OpenShift cluster. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The operation returns properties of each OpenShift cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | The operation returns properties of a OpenShift cluster. |
