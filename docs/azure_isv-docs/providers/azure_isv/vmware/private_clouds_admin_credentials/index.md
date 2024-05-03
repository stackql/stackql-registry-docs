---
title: private_clouds_admin_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds_admin_credentials
  - vmware
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
<tr><td><b>Name</b></td><td><code>private_clouds_admin_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware.private_clouds_admin_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nsxtPassword" /> | `string` | NSX-T Manager password |
| <CopyableCode code="nsxtUsername" /> | `string` | NSX-T Manager username |
| <CopyableCode code="vcenterPassword" /> | `string` | vCenter admin password |
| <CopyableCode code="vcenterUsername" /> | `string` | vCenter admin username |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="privateCloudName, resourceGroupName, subscriptionId" /> |
