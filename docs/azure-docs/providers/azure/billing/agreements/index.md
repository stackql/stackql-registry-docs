---
title: agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - agreements
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

Creates, updates, deletes, gets or lists a <code>agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.agreements" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agreements', value: 'view', },
        { label: 'agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="acceptance_mode" /> | `text` | field from the `properties` object |
| <CopyableCode code="agreementName" /> | `text` | field from the `properties` object |
| <CopyableCode code="agreement_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="category" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="effective_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="lead_billing_account_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="participants" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | An agreement. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agreementName, billingAccountName" /> | Gets an agreement by ID. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the agreements for a billing account. |

## `SELECT` examples

Lists the agreements for a billing account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_agreements', value: 'view', },
        { label: 'agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
acceptance_mode,
agreementName,
agreement_link,
billingAccountName,
billing_profile_info,
category,
display_name,
effective_date,
expiration_date,
lead_billing_account_name,
participants,
status,
tags
FROM azure.billing.vw_agreements
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.agreements
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>

