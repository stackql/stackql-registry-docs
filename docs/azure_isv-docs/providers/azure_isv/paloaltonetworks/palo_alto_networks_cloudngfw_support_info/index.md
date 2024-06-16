---
title: palo_alto_networks_cloudngfw_support_info
hide_title: false
hide_table_of_contents: false
keywords:
  - palo_alto_networks_cloudngfw_support_info
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
<tr><td><b>Name</b></td><td><code>palo_alto_networks_cloudngfw_support_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloaltonetworks.palo_alto_networks_cloudngfw_support_info" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="accountId" /> | `string` | Support account associated with given resource |
| <CopyableCode code="accountRegistrationStatus" /> | `string` | Registration status |
| <CopyableCode code="credits" /> | `integer` | credits purchased, unit per hour |
| <CopyableCode code="endDateForCredits" /> | `string` | date in format yyyy-mm-dd |
| <CopyableCode code="freeTrial" /> | `string` | Enable status |
| <CopyableCode code="freeTrialCreditLeft" /> | `integer` | Free trial credit remaining |
| <CopyableCode code="freeTrialDaysLeft" /> | `integer` | Free trial days remaining |
| <CopyableCode code="helpURL" /> | `string` | URL for paloaltonetworks live community |
| <CopyableCode code="hubUrl" /> | `string` | URL for Strata Cloud Manager |
| <CopyableCode code="monthlyCreditLeft" /> | `integer` | monthly credit is computed as credits * days in calendar month |
| <CopyableCode code="productSerial" /> | `string` | product Serial associated with given resource |
| <CopyableCode code="productSku" /> | `string` | product SKU associated with given resource |
| <CopyableCode code="registerURL" /> | `string` | URL for registering product in paloaltonetworks Customer Service Portal |
| <CopyableCode code="startDateForCredits" /> | `string` | date in format yyyy-mm-dd |
| <CopyableCode code="supportURL" /> | `string` | URL for paloaltonetworks Customer Service Portal |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |
