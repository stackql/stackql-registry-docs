---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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

Creates, updates, deletes, gets or lists a <code>accounts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.accounts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_status_reason_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_sub_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="account_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="agreement_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_relationship_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_no_billing_profiles" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_read_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="notification_email_address" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_billing_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="qualifications" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="sold_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="tax_ids" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A billing account. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Gets a billing account by its ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists the billing accounts that a user has access to. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="billingAccountName" /> | Updates the properties of a billing account. Currently, displayName and address can be updated for billing accounts with agreement type Microsoft Customer Agreement. Currently address and notification email address can be updated for billing accounts with agreement type Microsoft Online Services Agreement. Currently, purchase order number can be edited for billing accounts with agreement type Enterprise Agreement. |
| <CopyableCode code="add_payment_terms" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Adds payment terms to all the billing profiles under the billing account. Currently, payment terms can be added only on billing accounts that have Agreement Type as 'Microsoft Customer Agreement' and AccountType as 'Enterprise'. This action needs pre-authorization and only Field Sellers are authorized to add the payment terms and is not a self-serve action. |
| <CopyableCode code="cancel_payment_terms" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Cancels all the payment terms on billing account that falls after the cancellation date in the request. Currently, cancel payment terms is only served by admin actions and is not a self-serve action. |
| <CopyableCode code="confirm_transition" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Gets the transition details for a billing account that has transitioned from agreement type Microsoft Online Services Program to agreement type Microsoft Customer Agreement. |
| <CopyableCode code="validate_payment_terms" /> | `EXEC` | <CopyableCode code="billingAccountName" /> | Validates payment terms on a billing account with agreement type 'Microsoft Customer Agreement' and account type 'Enterprise'. |

## `SELECT` examples

Lists the billing accounts that a user has access to.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_accounts', value: 'view', },
        { label: 'accounts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_status,
account_status_reason_code,
account_sub_type,
account_type,
agreement_type,
billingAccountName,
billing_relationship_types,
display_name,
enrollment_details,
has_no_billing_profiles,
has_read_access,
notification_email_address,
primary_billing_tenant_id,
provisioning_state,
qualifications,
registration_number,
sold_to,
tags,
tax_ids
FROM azure.billing.vw_accounts
;
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.accounts
;
```
</TabItem></Tabs>


## `UPDATE` example

Updates a <code>accounts</code> resource.

```sql
/*+ update */
UPDATE azure.billing.accounts
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
billingAccountName = '{{ billingAccountName }}';
```
