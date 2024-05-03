---
title: endpoints_managed_proxy_details
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints_managed_proxy_details
  - hybrid_connectivity
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
<tr><td><b>Name</b></td><td><code>endpoints_managed_proxy_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.endpoints_managed_proxy_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expiresOn" /> | `integer` | The expiration time of short lived proxy name in unix epoch. |
| <CopyableCode code="proxy" /> | `string` | The short lived proxy name. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri, data__service" /> |
