---
title: local_rulestacks_support_info
hide_title: false
hide_table_of_contents: false
keywords:
  - local_rulestacks_support_info
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

Creates, updates, deletes, gets or lists a <code>local_rulestacks_support_info</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>local_rulestacks_support_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.paloalto.local_rulestacks_support_info" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="localRulestackName, resourceGroupName, subscriptionId" /> | support info for rulestack. |

## `SELECT` examples

support info for rulestack.


```sql
SELECT
accountId,
accountRegistered,
freeTrial,
freeTrialCreditLeft,
freeTrialDaysLeft,
helpURL,
productSerial,
productSku,
registerURL,
supportURL,
userDomainSupported,
userRegistered
FROM azure_isv.paloalto.local_rulestacks_support_info
WHERE localRulestackName = '{{ localRulestackName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```