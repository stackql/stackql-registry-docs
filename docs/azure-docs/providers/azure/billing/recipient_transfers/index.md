---
title: recipient_transfers
hide_title: false
hide_table_of_contents: false
keywords:
  - recipient_transfers
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

Creates, updates, deletes, gets or lists a <code>recipient_transfers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipient_transfers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.recipient_transfers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recipient_transfers', value: 'view', },
        { label: 'recipient_transfers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="allowed_product_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="canceled_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_transfer_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="initiator_customer_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="initiator_email_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="recipient_email_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="reseller_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="reseller_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="supported_accounts" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="transferName" /> | `text` | field from the `properties` object |
| <CopyableCode code="transfer_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Transfer Details. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="transferName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> |  |
| <CopyableCode code="accept" /> | `EXEC` | <CopyableCode code="transferName" /> |  |
| <CopyableCode code="decline" /> | `EXEC` | <CopyableCode code="transferName" /> |  |
| <CopyableCode code="validate" /> | `EXEC` | <CopyableCode code="transferName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_recipient_transfers', value: 'view', },
        { label: 'recipient_transfers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
allowed_product_type,
canceled_by,
customer_tenant_id,
detailed_transfer_status,
expiration_time,
initiator_customer_type,
initiator_email_id,
recipient_email_id,
reseller_id,
reseller_name,
supported_accounts,
tags,
transferName,
transfer_status
FROM azure.billing.vw_recipient_transfers
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.recipient_transfers
;
```
</TabItem></Tabs>

