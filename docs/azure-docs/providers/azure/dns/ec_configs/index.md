---
title: ec_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - ec_configs
  - dns
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
<tr><td><b>Name</b></td><td><code>ec_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.ec_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the DNSSEC configuration. |
| <CopyableCode code="name" /> | `string` | The name of the DNSSEC configuration. |
| <CopyableCode code="etag" /> | `string` | The etag of the DNSSEC configuration. |
| <CopyableCode code="properties" /> | `object` | Represents the DNSSEC properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the DNSSEC configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Gets the DNSSEC configuration. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Creates or updates the DNSSEC configuration on a DNS zone. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> | Deletes the DNSSEC configuration on a DNS zone. This operation cannot be undone. |
