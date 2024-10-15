---
title: palo_alto_networks_cloudngfw_support_info
hide_title: false
hide_table_of_contents: false
keywords:
  - palo_alto_networks_cloudngfw_support_info
  - paloalto
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>palo_alto_networks_cloudngfw_support_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>palo_alto_networks_cloudngfw_support_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.palo_alto_networks_cloudngfw_support_info" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
accountId,
accountRegistrationStatus,
credits,
endDateForCredits,
freeTrial,
freeTrialCreditLeft,
freeTrialDaysLeft,
helpURL,
hubUrl,
monthlyCreditLeft,
productSerial,
productSku,
registerURL,
startDateForCredits,
supportURL
FROM azure_isv.paloalto.palo_alto_networks_cloudngfw_support_info
WHERE subscriptionId = '{{ subscriptionId }}';
```