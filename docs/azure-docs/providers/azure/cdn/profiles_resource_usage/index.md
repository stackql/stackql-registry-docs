---
title: profiles_resource_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles_resource_usage
  - cdn
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
<tr><td><b>Name</b></td><td><code>profiles_resource_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.profiles_resource_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="currentValue" /> | `integer` | Actual value of usage on the specified resource type. |
| <CopyableCode code="limit" /> | `integer` | Quota of the specified resource type. |
| <CopyableCode code="resourceType" /> | `string` | Resource type for which the usage is provided. |
| <CopyableCode code="unit" /> | `string` | Unit of the usage. e.g. count. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="profileName, resourceGroupName, subscriptionId" /> |
