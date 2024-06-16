---
title: servers_details
hide_title: false
hide_table_of_contents: false
keywords:
  - servers_details
  - analysis_services
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
<tr><td><b>Name</b></td><td><code>servers_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.analysis_services.servers_details" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the Analysis Services resource. |
| <CopyableCode code="name" /> | `string` | The name of the Analysis Services resource. |
| <CopyableCode code="location" /> | `string` | Location of the Analysis Services resource. |
| <CopyableCode code="properties" /> | `object` | Properties of Analysis Services resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for Analysis Services resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the Analysis Services resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> |
