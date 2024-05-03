---
title: azure_dev_ops_repo
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_dev_ops_repo
  - security_devops
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
<tr><td><b>Name</b></td><td><code>azure_dev_ops_repo</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_devops.azure_dev_ops_repo" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, azureDevOpsRepoName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list_by_connector" /> | `SELECT` | <CopyableCode code="azureDevOpsConnectorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, azureDevOpsRepoName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list_by_connector" /> | `EXEC` | <CopyableCode code="azureDevOpsConnectorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="azureDevOpsConnectorName, azureDevOpsOrgName, azureDevOpsProjectName, azureDevOpsRepoName, resourceGroupName, subscriptionId" /> |
