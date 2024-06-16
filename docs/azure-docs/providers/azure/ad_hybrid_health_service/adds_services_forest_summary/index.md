---
title: adds_services_forest_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_forest_summary
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>adds_services_forest_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_forest_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="domainCount" /> | `integer` | The domain count. |
| <CopyableCode code="domains" /> | `array` | The list of domain controller names. |
| <CopyableCode code="forestName" /> | `string` | The forest name. |
| <CopyableCode code="monitoredDcCount" /> | `integer` | The number of domain controllers that are monitored by Azure Active Directory Connect Health. |
| <CopyableCode code="siteCount" /> | `integer` | The site count. |
| <CopyableCode code="sites" /> | `array` | The list of site names. |
| <CopyableCode code="totalDcCount" /> | `integer` | The total domain controllers. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceName" /> |
