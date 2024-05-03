---
title: certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - certificates
  - nginx
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
<tr><td><b>Name</b></td><td><code>certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.nginx.certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="location" /> | `string` |  |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, deploymentName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, deploymentName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, deploymentName, resourceGroupName, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="deploymentName, resourceGroupName, subscriptionId" /> |
