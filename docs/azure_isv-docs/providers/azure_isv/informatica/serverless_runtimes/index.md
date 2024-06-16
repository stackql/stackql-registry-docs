---
title: serverless_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - serverless_runtimes
  - informatica
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
<tr><td><b>Name</b></td><td><code>serverless_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.informatica.serverless_runtimes" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Get a InformaticaServerlessRuntimeResource |
| <CopyableCode code="list_by_informatica_organization_resource" /> | `SELECT` | <CopyableCode code="organizationName, resourceGroupName, subscriptionId" /> | List InformaticaServerlessRuntimeResource resources by InformaticaOrganizationResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Create a InformaticaServerlessRuntimeResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Delete a InformaticaServerlessRuntimeResource |
| <CopyableCode code="check_dependencies" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Checks all dependencies for a serverless runtime resource |
| <CopyableCode code="serverless_resource_by_id" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Returns a serverless runtime resource by ID |
| <CopyableCode code="start_failed_serverless_runtime" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Starts a failed runtime resource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="organizationName, resourceGroupName, serverlessRuntimeName, subscriptionId" /> | Update a InformaticaServerlessRuntimeResource |
