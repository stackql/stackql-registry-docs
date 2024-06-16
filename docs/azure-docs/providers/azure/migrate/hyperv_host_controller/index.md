---
title: hyperv_host_controller
hide_title: false
hide_table_of_contents: false
keywords:
  - hyperv_host_controller
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
<tr><td><b>Name</b></td><td><code>hyperv_host_controller</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.migrate.hyperv_host_controller" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hostName, resourceGroupName, siteName, subscriptionId" /> | Get a HypervHost |
| <CopyableCode code="list_by_hyperv_site" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List HypervHost resources by HypervSite |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="hostName, resourceGroupName, siteName, subscriptionId" /> | Create a HypervHost |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hostName, resourceGroupName, siteName, subscriptionId" /> | Delete a HypervHost |
