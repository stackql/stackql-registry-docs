---
title: springbootservers
hide_title: false
hide_table_of_contents: false
keywords:
  - springbootservers
  - off_azure_springboot
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>springbootservers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.off_azure_springboot.springbootservers" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | List springbootservers resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, siteName, subscriptionId" /> | List springbootservers resource by resourceGroup |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="siteName, subscriptionId" /> | List springbootservers resource by subscription |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | Create springbootservers resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | Delete springbootservers resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="resourceGroupName, siteName, springbootserversName, subscriptionId" /> | Update springbootservers resource. |
