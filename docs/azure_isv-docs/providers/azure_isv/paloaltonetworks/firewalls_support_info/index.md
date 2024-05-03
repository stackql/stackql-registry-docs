---
title: firewalls_support_info
hide_title: false
hide_table_of_contents: false
keywords:
  - firewalls_support_info
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
<tr><td><b>Name</b></td><td><code>firewalls_support_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.firewalls_support_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountId" /> | `string` | Support account associated with given resource |
| <CopyableCode code="accountRegistered" /> | `string` | Boolean Enum |
| <CopyableCode code="freeTrial" /> | `string` | Boolean Enum |
| <CopyableCode code="freeTrialCreditLeft" /> | `integer` | Free trial credit remaining |
| <CopyableCode code="freeTrialDaysLeft" /> | `integer` | Free trial days remaining |
| <CopyableCode code="helpURL" /> | `string` | URL for paloaltonetworks live community |
| <CopyableCode code="productSerial" /> | `string` | product Serial associated with given resource |
| <CopyableCode code="productSku" /> | `string` | product SKU associated with given resource |
| <CopyableCode code="registerURL" /> | `string` | URL for registering product in paloaltonetworks Customer Service Portal |
| <CopyableCode code="supportURL" /> | `string` | URL for paloaltonetworks Customer Service Portal |
| <CopyableCode code="userDomainSupported" /> | `string` | Boolean Enum |
| <CopyableCode code="userRegistered" /> | `string` | Boolean Enum |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallName, resourceGroupName, subscriptionId" /> |
