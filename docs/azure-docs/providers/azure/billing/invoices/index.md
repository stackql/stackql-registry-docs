---
title: invoices
hide_title: false
hide_table_of_contents: false
keywords:
  - invoices
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

Creates, updates, deletes, gets or lists a <code>invoices</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invoices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.invoices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | An invoice. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="invoiceName" /> | Gets an invoice by ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="get_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName, invoiceName" /> | Gets an invoice by billing account name and ID. The operation is supported for all billing account types. |
| <CopyableCode code="get_by_billing_subscription" /> | `SELECT` | <CopyableCode code="invoiceName, subscriptionId" /> | Gets an invoice by subscription ID and invoice ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the invoices for a billing account for a given start date and end date. The operation is supported for all billing account types. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Lists the invoices for a billing profile for a given start date and end date. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="list_by_billing_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists the invoices for a subscription. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="amend" /> | `EXEC` | <CopyableCode code="billingAccountName, invoiceName" /> | Regenerate an invoice by billing account name and invoice name. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="download_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName, invoiceName" /> | Gets a URL to download an invoice document. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement, Microsoft Customer Agreement or Enterprise Agreement. |
| <CopyableCode code="download_by_billing_subscription" /> | `EXEC` | <CopyableCode code="invoiceName, subscriptionId" /> | Gets a URL to download an invoice by billing subscription. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="download_documents_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="download_documents_by_billing_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Gets a URL to download multiple invoice documents (invoice pdf, tax receipts, credit notes) as a zip file. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement. |
| <CopyableCode code="download_summary_by_billing_account" /> | `EXEC` | <CopyableCode code="billingAccountName, invoiceName" /> | Gets a URL to download the summary document for an invoice. The operation is supported for billing accounts with agreement type Enterprise Agreement. |

## `SELECT` examples

Gets an invoice by ID. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.


```sql
SELECT
properties,
tags
FROM azure.billing.invoices
WHERE invoiceName = '{{ invoiceName }}';
```