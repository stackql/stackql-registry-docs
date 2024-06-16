---
title: private_clouds
hide_title: false
hide_table_of_contents: false
keywords:
  - private_clouds
  - vmware_cloud_simple
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
<tr><td><b>Name</b></td><td><code>private_clouds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.private_clouds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Azure Id, e.g. "/subscriptions/4da99247-a172-4ed6-8ae9-ebed2d12f839/providers/Microsoft.VMwareCloudSimple/privateClouds/cloud123" |
| <CopyableCode code="name" /> | `string` | Private cloud name |
| <CopyableCode code="location" /> | `string` | Location where private cloud created, e.g "westus" |
| <CopyableCode code="properties" /> | `object` | Properties of private |
| <CopyableCode code="type" /> | `string` | Azure Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, pcName, regionId, subscriptionId" /> | Returns private cloud by its name |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, regionId, subscriptionId" /> | Returns list of private clouds in particular region |
