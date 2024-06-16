---
title: extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - extensions
  - kubernetes_configuration
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
<tr><td><b>Name</b></td><td><code>extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.extensions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of an Extension resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Gets Kubernetes Cluster Extension. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Extensions in the cluster. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Create a new Kubernetes Cluster Extension. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Delete a Kubernetes Cluster Extension. This will cause the Agent to Uninstall the extension from the cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, extensionName, resourceGroupName, subscriptionId" /> | Patch an existing Kubernetes Cluster Extension. |
