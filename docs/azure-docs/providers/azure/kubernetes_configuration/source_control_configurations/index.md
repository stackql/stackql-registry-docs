---
title: source_control_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control_configurations
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
<tr><td><b>Name</b></td><td><code>source_control_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.kubernetes_configuration.source_control_configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties to create a Source Control Configuration resource |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId" /> | Gets details of the Source Control Configuration. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Source Control Configurations. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId" /> | Create a new Kubernetes Source Control Configuration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, sourceControlConfigurationName, subscriptionId" /> | This will delete the YAML file used to set up the Source control configuration, thus stopping future sync from the source repo. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="clusterName, clusterResourceName, clusterRp, resourceGroupName, subscriptionId" /> | List all Source Control Configurations. |
