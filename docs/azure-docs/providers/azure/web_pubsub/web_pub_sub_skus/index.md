---
title: web_pub_sub_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_skus
  - web_pubsub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.web_pubsub.web_pub_sub_skus" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the SKU. E.g. P3. It is typically a letter+number code |
| <CopyableCode code="capacity" /> | `integer` | If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted. |
| <CopyableCode code="family" /> | `string` | If the service has different generations of hardware, for the same SKU, then that can be captured here. |
| <CopyableCode code="size" /> | `string` | The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code.  |
| <CopyableCode code="tier" /> | `string` | This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> |
