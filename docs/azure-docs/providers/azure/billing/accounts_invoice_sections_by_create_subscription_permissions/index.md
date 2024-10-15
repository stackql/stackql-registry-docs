---
title: accounts_invoice_sections_by_create_subscription_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_invoice_sections_by_create_subscription_permissions
  - billing
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

Creates, updates, deletes, gets or lists a <code>accounts_invoice_sections_by_create_subscription_permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_invoice_sections_by_create_subscription_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.accounts_invoice_sections_by_create_subscription_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingProfileDisplayName" /> | `string` | The name of the billing profile. |
| <CopyableCode code="billingProfileId" /> | `string` | The fully qualified ID that uniquely identifies a billing profile. |
| <CopyableCode code="billingProfileSpendingLimit" /> | `string` | The billing profile spending limit. |
| <CopyableCode code="billingProfileStatus" /> | `string` | The status of the billing profile. |
| <CopyableCode code="billingProfileStatusReasonCode" /> | `string` | Reason for the specified billing profile status. |
| <CopyableCode code="billingProfileSystemId" /> | `string` | The system generated unique identifier for a billing profile. |
| <CopyableCode code="enabledAzurePlans" /> | `array` | Enabled azure plans for the associated billing profile. |
| <CopyableCode code="invoiceSectionDisplayName" /> | `string` | The name of the invoice section. |
| <CopyableCode code="invoiceSectionId" /> | `string` | The fully qualified ID that uniquely identifies an invoice section. |
| <CopyableCode code="invoiceSectionSystemId" /> | `string` | The system generated unique identifier for an invoice section. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the invoice sections for which the user has permission to create Azure subscriptions. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the invoice sections for which the user has permission to create Azure subscriptions. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.


```sql
SELECT
billingProfileDisplayName,
billingProfileId,
billingProfileSpendingLimit,
billingProfileStatus,
billingProfileStatusReasonCode,
billingProfileSystemId,
enabledAzurePlans,
invoiceSectionDisplayName,
invoiceSectionId,
invoiceSectionSystemId
FROM azure.billing.accounts_invoice_sections_by_create_subscription_permissions
WHERE billingAccountName = '{{ billingAccountName }}';
```