---
title: session_host_managements
hide_title: false
hide_table_of_contents: false
keywords:
  - session_host_managements
  - desktop_virtualization
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
<tr><td><b>Name</b></td><td><code>session_host_managements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.desktop_virtualization.session_host_managements" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Session host Managements of HostPool. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Get a SessionHostManagement. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId, data__properties" /> | Create or update a SessionHostManagement. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="hostPoolName, resourceGroupName, subscriptionId" /> | Update a SessionHostManagement. |
