---
title: application_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - application_resources
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
<tr><td><b>Name</b></td><td><code>application_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.integration_environment.application_resources" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Get a ApplicationResource |
| <CopyableCode code="list_by_application" /> | `SELECT` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | List ApplicationResource resources by Application |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Create a ApplicationResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Delete a ApplicationResource |
| <CopyableCode code="_list_by_application" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, spaceName, subscriptionId" /> | List ApplicationResource resources by Application |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="applicationName, resourceGroupName, resourceName, spaceName, subscriptionId" /> | Update a ApplicationResource |
