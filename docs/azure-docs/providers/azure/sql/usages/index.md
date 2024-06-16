---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - sql
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
<tr><td><b>Name</b></td><td><code>usages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `object` | ARM Usage Name |
| <CopyableCode code="currentValue" /> | `integer` | Usage current value. |
| <CopyableCode code="limit" /> | `integer` | Usage limit. |
| <CopyableCode code="requestedLimit" /> | `integer` | Usage requested limit. |
| <CopyableCode code="type" /> | `string` | Resource type. |
| <CopyableCode code="unit" /> | `string` | Usage unit. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_instance_pool" /> | `SELECT` | <CopyableCode code="instancePoolName, resourceGroupName, subscriptionId" /> |
