---
title: dns_private_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - dns_private_zones
  - oracle
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
<tr><td><b>Name</b></td><td><code>dns_private_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.oracle.dns_private_zones" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dnsprivatezonename, location, subscriptionId" /> | Get a DnsPrivateZone |
| <CopyableCode code="list_by_location" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | List DnsPrivateZone resources by Location |
