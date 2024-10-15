---
title: transfers
hide_title: false
hide_table_of_contents: false
keywords:
  - transfers
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

Creates, updates, deletes, gets or lists a <code>transfers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transfers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.transfers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_transfers', value: 'view', },
        { label: 'transfers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="canceled_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_transfer_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="initiator_email_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoiceSectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recipient_email_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="transferName" /> | `text` | field from the `properties` object |
| <CopyableCode code="transfer_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Transfer details |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName, transferName" /> | Gets a transfer request by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName" /> | Lists the transfer requests for an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName, transferName" /> | Cancels a transfer request. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |
| <CopyableCode code="initiate" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName, invoiceSectionName, transferName" /> | Sends a request to a user in another billing account to transfer billing ownership of their subscriptions. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement. |

## `SELECT` examples

Lists the transfer requests for an invoice section. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_transfers', value: 'view', },
        { label: 'transfers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
billingAccountName,
billingProfileName,
canceled_by,
detailed_transfer_status,
expiration_time,
initiator_email_id,
invoiceSectionName,
recipient_email_id,
tags,
transferName,
transfer_status
FROM azure.billing.vw_transfers
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.transfers
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}'
AND invoiceSectionName = '{{ invoiceSectionName }}';
```
</TabItem></Tabs>

