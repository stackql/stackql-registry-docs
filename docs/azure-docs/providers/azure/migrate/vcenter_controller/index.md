---
title: vcenter_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - vcenter_controller
  - migrate
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
<tr><td><b>Name</b></td><td><code>vcenter_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.vcenter_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, vcenterName" /> | Get a Vcenter |
| <CopyableCode code="list_by_vmware_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List Vcenter resources by VmwareSite |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, vcenterName" /> | Create a Vcenter |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, subscriptionId, vcenterName" /> | Delete a Vcenter |
