---
title: palo_alto_networks_cloudngfw_product_serial_number_status
hide_title: false
hide_table_of_contents: false
keywords:
  - palo_alto_networks_cloudngfw_product_serial_number_status
  - paloaltonetworks
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
<tr><td><b>Name</b></td><td><code>palo_alto_networks_cloudngfw_product_serial_number_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.palo_alto_networks_cloudngfw_product_serial_number_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="serialNumber" /> | `string` | product Serial associated with given resource |
| <CopyableCode code="status" /> | `string` | allocation status of the product serial number |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
