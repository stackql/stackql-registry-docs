---
title: flux_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - flux_configurations
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
<tr><td><b>Name</b></td><td><code>flux_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.flux_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties to create a Flux Configuration resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | Gets details of the Flux Configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Flux Configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | Create a new Kubernetes Flux Configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | This will delete the YAML file used to set up the Flux Configuration, thus stopping future sync from the source repo. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Flux Configurations. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, fluxConfigurationName, resourceGroupName, subscriptionId" /> | Update an existing Kubernetes Flux Configuration. |
