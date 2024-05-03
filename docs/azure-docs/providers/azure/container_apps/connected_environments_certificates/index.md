---
title: connected_environments_certificates
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments_certificates
  - container_apps
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
<tr><td><b>Name</b></td><td><code>connected_environments_certificates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments_certificates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Certificate resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="certificateName, connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Patches a certificate. Currently only patching of tags is supported |
