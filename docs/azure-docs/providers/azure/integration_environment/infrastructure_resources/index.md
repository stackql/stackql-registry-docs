---
title: infrastructure_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - infrastructure_resources
  - integration_environment
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
<tr><td><b>Name</b></td><td><code>infrastructure_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.infrastructure_resources" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Get a InfrastructureResource |
| <CopyableCode code="list_by_space" /> | `SELECT` | <CopyableCode code="resourceGroupName, spaceName, subscriptionId" /> | List InfrastructureResource resources by Space |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Create a InfrastructureResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Delete a InfrastructureResource |
| <CopyableCode code="_list_by_space" /> | `EXEC` | <CopyableCode code="resourceGroupName, spaceName, subscriptionId" /> | List InfrastructureResource resources by Space |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="infrastructureResourceName, resourceGroupName, spaceName, subscriptionId" /> | Update a InfrastructureResource |
