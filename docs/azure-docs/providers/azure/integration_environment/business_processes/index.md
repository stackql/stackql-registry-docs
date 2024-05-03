---
title: business_processes
hide_title: false
hide_table_of_contents: false
keywords:
  - business_processes
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
<tr><td><b>Name</b></td><td><code>business_processes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.business_processes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Get a BusinessProcess |
| <CopyableCode code="list_by_application" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | List BusinessProcess resources by Application |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Create a BusinessProcess |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Delete a BusinessProcess |
| <CopyableCode code="_list_by_application" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | List BusinessProcess resources by Application |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="applicationName, businessProcessName, resourceGroupName, spaceName, subscriptionId" /> | Update a BusinessProcess |
