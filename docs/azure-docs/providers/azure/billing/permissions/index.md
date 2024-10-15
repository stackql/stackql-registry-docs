---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
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

Creates, updates, deletes, gets or lists a <code>permissions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions" /> | `array` | The set of actions that the caller is allowed to perform. |
| <CopyableCode code="notActions" /> | `array` | The set of actions that the caller is not allowed to perform. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the billing permissions the caller has on a billing account. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the billing permissions the caller has on a billing profile. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | Lists the billing permissions the caller has for a customer. |
| <CopyableCode code="list_by_customer_at_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, customerName" /> | Lists the billing permissions the caller has for a customer at billing account level. |
| <CopyableCode code="list_by_department" /> | `SELECT` | <CopyableCode code="billingAccountName, departmentName" /> | Lists the billing permissions the caller has for a department. |
| <CopyableCode code="list_by_enrollment_account" /> | `SELECT` | <CopyableCode code="billingAccountName, enrollmentAccountName" /> | Lists the billing permissions the caller has for an enrollment account. |
| <CopyableCode code="check_access_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Provides a list of check access response objects for a billing account. |
| <CopyableCode code="check_access_by_billing_profile" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName" /> | Provides a list of check access response objects for a billing profile. |
| <CopyableCode code="check_access_by_customer" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | Provides a list of check access response objects for a customer. |
| <CopyableCode code="check_access_by_department" /> | `EXEC` | <CopyableCode code="billingAccountName, departmentName" /> | Provides a list of check access response objects for a department. |
| <CopyableCode code="check_access_by_enrollment_account" /> | `EXEC` | <CopyableCode code="billingAccountName, enrollmentAccountName" /> | Provides a list of check access response objects for an enrollment account. |
| <CopyableCode code="check_access_by_invoice_section" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Provides a list of check access response objects for an invoice section. |

## `SELECT` examples

Lists the billing permissions the caller has on a billing account.


```sql
SELECT
actions,
notActions
FROM azure.billing.permissions
WHERE billingAccountName = '{{ billingAccountName }}';
```