---
title: azure_dev_ops_orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_dev_ops_orgs
  - security
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
<tr><td><b>Name</b></td><td><code>azure_dev_ops_orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.azure_dev_ops_orgs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Azure DevOps Organization properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="orgName, resourceGroupName, securityConnectorName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, securityConnectorName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="orgName, resourceGroupName, securityConnectorName, subscriptionId" /> |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="orgName, resourceGroupName, securityConnectorName, subscriptionId" /> |
