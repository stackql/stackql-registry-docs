---
title: business_services
hide_title: false
hide_table_of_contents: false
keywords:
  - business_services
  - service_dependencies
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>business_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.service_dependencies.business_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="dependent_service" /> | `object` | The reference to the service that is dependent on the Business Service. |
| <CopyableCode code="supporting_service" /> | `object` | The reference to the service that supports the Business Service. |
| <CopyableCode code="type" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_business_service_service_dependencies" /> | `SELECT` | <CopyableCode code="id" /> |
| <CopyableCode code="_get_business_service_service_dependencies" /> | `EXEC` | <CopyableCode code="id" /> |
