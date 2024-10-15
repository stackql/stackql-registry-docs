---
title: permissions_by_invoice_sections
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions_by_invoice_sections
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

Creates, updates, deletes, gets or lists a <code>permissions_by_invoice_sections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions_by_invoice_sections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.permissions_by_invoice_sections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actions" /> | `array` | The set of actions that the caller is allowed to perform. |
| <CopyableCode code="notActions" /> | `array` | The set of actions that the caller is not allowed to perform. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the billing permissions the caller has for an invoice section. |

## `SELECT` examples

Lists the billing permissions the caller has for an invoice section.


```sql
SELECT
actions,
notActions
FROM azure.billing.permissions_by_invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```