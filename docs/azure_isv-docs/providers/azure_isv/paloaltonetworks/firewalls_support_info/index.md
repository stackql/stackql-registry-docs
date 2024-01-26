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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewalls_support_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.paloaltonetworks.firewalls_support_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accountId` | `string` | Support account associated with given resource |
| `accountRegistered` | `string` | Boolean Enum |
| `freeTrial` | `string` | Boolean Enum |
| `freeTrialCreditLeft` | `integer` | Free trial credit remaining |
| `freeTrialDaysLeft` | `integer` | Free trial days remaining |
| `helpURL` | `string` | URL for paloaltonetworks live community |
| `productSerial` | `string` | product Serial associated with given resource |
| `productSku` | `string` | product SKU associated with given resource |
| `registerURL` | `string` | URL for registering product in paloaltonetworks Customer Service Portal |
| `supportURL` | `string` | URL for paloaltonetworks Customer Service Portal |
| `userDomainSupported` | `string` | Boolean Enum |
| `userRegistered` | `string` | Boolean Enum |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `firewallName, resourceGroupName, subscriptionId` |
