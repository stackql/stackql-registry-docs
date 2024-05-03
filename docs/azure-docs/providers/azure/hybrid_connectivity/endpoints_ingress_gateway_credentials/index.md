---
title: endpoints_ingress_gateway_credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints_ingress_gateway_credentials
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
<tr><td><b>Name</b></td><td><code>endpoints_ingress_gateway_credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.endpoints_ingress_gateway_credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ingress" /> | `object` | Ingress gateway profile |
| <CopyableCode code="relay" /> | `object` | Azure relay hybrid connection access properties |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="endpointName, resourceUri" /> |
