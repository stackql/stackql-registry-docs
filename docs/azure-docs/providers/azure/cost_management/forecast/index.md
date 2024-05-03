---
title: forecast
hide_title: false
hide_table_of_contents: false
keywords:
  - forecast
  - cost_management
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
<tr><td><b>Name</b></td><td><code>forecast</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.forecast" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="external_cloud_provider_usage" /> | `EXEC` | <CopyableCode code="externalCloudProviderId, externalCloudProviderType, data__dataset, data__timeframe, data__type" /> | Lists the forecast charges for external cloud provider type defined. |
| <CopyableCode code="usage" /> | `EXEC` | <CopyableCode code="scope, data__dataset, data__timeframe, data__type" /> | Lists the forecast charges for scope defined. |
