---
title: subscriptions_by_invoice_sections
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions_by_invoice_sections
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

Creates, updates, deletes, gets or lists a <code>subscriptions_by_invoice_sections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions_by_invoice_sections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.subscriptions_by_invoice_sections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The billing properties of a subscription. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the subscriptions that are billed to an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the subscriptions that are billed to an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.


```sql
SELECT
properties,
tags
FROM azure.billing.subscriptions_by_invoice_sections
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```