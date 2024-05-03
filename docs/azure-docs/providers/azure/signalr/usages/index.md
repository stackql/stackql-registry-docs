---
title: usages
hide_title: false
hide_table_of_contents: false
keywords:
  - usages
  - signalr
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.signalr.usages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ARM resource id |
| <CopyableCode code="name" /> | `object` | Localizable String object containing the name and a localized value. |
| <CopyableCode code="currentValue" /> | `integer` | Current value for the usage quota. |
| <CopyableCode code="limit" /> | `integer` | The maximum permitted value for the usage quota. If there is no limit, this value will be -1. |
| <CopyableCode code="unit" /> | `string` | Representing the units of the usage quota. Possible values are: Count, Bytes, Seconds, Percent, CountPerSecond, BytesPerSecond. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> |
