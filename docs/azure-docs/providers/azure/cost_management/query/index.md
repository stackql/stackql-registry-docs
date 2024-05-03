---
title: query
hide_title: false
hide_table_of_contents: false
keywords:
  - query
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
<tr><td><b>Name</b></td><td><code>query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.query" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="usage" /> | `EXEC` | <CopyableCode code="scope, data__dataset, data__timeframe, data__type" /> | Query the usage data for scope defined. |
| <CopyableCode code="usage_by_external_cloud_provider_type" /> | `EXEC` | <CopyableCode code="externalCloudProviderId, externalCloudProviderType, data__dataset, data__timeframe, data__type" /> | Query the usage data for external cloud provider type defined. |
