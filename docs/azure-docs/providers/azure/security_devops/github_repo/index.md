---
title: github_repo
hide_title: false
hide_table_of_contents: false
keywords:
  - github_repo
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
<tr><td><b>Name</b></td><td><code>github_repo</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security_devops.github_repo" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gitHubConnectorName, gitHubOwnerName, gitHubRepoName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="gitHubConnectorName, gitHubOwnerName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list_by_connector" /> | `SELECT` | <CopyableCode code="gitHubConnectorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="gitHubConnectorName, gitHubOwnerName, gitHubRepoName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="gitHubConnectorName, gitHubOwnerName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list_by_connector" /> | `EXEC` | <CopyableCode code="gitHubConnectorName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="gitHubConnectorName, gitHubOwnerName, gitHubRepoName, resourceGroupName, subscriptionId" /> |
