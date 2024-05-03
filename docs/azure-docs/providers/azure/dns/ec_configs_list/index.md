---
title: ec_configs_list
hide_title: false
hide_table_of_contents: false
keywords:
  - ec_configs_list
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
<tr><td><b>Name</b></td><td><code>ec_configs_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dns.ec_configs_list" /></td></tr>
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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_by_dns_zone" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> |
| <CopyableCode code="_list_by_dns_zone" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, zoneName" /> |
