---
title: afd_endpoints_resource_usage
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_endpoints_resource_usage
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
<tr><td><b>Name</b></td><td><code>afd_endpoints_resource_usage</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cdn.afd_endpoints_resource_usage" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextLink" /> | `string` | URL to get the next set of results. |
| <CopyableCode code="value" /> | `array` | The list of resource usages. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="endpointName, profileName, resourceGroupName, subscriptionId" /> |
