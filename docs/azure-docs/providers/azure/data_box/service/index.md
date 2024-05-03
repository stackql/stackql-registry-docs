---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - data_box
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_box.service" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="region_configuration" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | This API provides configuration details specific to given region/location at Subscription level. |
| <CopyableCode code="region_configuration_by_resource_group" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId" /> | This API provides configuration details specific to given region/location at Resource group level. |
| <CopyableCode code="validate_address" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__deviceType, data__shippingAddress, data__validationType" /> | [DEPRECATED NOTICE: This operation will soon be removed]. This method validates the customer shipping address and provide alternate addresses if any. |
| <CopyableCode code="validate_inputs" /> | `EXEC` | <CopyableCode code="location, subscriptionId, data__individualRequestDetails, data__validationCategory" /> | This method does all necessary pre-job creation validation under subscription. |
| <CopyableCode code="validate_inputs_by_resource_group" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__individualRequestDetails, data__validationCategory" /> | This method does all necessary pre-job creation validation under resource group. |
