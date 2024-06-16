---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.vmware_cloud_simple.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | User name model |
| <CopyableCode code="currentValue" /> | `integer` | The current usage value |
| <CopyableCode code="limit" /> | `integer` | limit of a given sku in a region for a subscription. The maximum permitted value for the usage quota. If there is no limit, this value will be -1 |
| <CopyableCode code="unit" /> | `string` | The usages' unit |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="api-version, regionId, subscriptionId" /> |
