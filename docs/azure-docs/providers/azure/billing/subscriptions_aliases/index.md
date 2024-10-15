---
title: subscriptions_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions_aliases
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

Creates, updates, deletes, gets or lists a <code>subscriptions_aliases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.subscriptions_aliases" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscriptions_aliases', value: 'view', },
        { label: 'subscriptions_aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aliasName" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_renew" /> | `text` | field from the `properties` object |
| <CopyableCode code="beneficiary" /> | `text` | field from the `properties` object |
| <CopyableCode code="beneficiary_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_frequency" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_profile_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumption_cost_center" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="customer_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_account_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="enrollment_account_subscription_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_section_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_month_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="month_to_date_charges" /> | `text` | field from the `properties` object |
| <CopyableCode code="next_billing_cycle_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="offer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="operation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_category" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="product_type_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_tenant_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="purchase_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="quantity" /> | `text` | field from the `properties` object |
| <CopyableCode code="renewal_term_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="reseller" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="suspension_reason_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="suspension_reasons" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_overrides" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="term_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="term_end_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="term_start_date" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A billing subscription alias. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="aliasName, billingAccountName" /> | Gets a subscription by its alias ID.  The operation is supported for seat based billing subscriptions. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the subscription aliases for a billing account. The operation is supported for seat based billing subscriptions. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="aliasName, billingAccountName" /> | Creates or updates a billing subscription by its alias ID.  The operation is supported for seat based billing subscriptions. |

## `SELECT` examples

Lists the subscription aliases for a billing account. The operation is supported for seat based billing subscriptions.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscriptions_aliases', value: 'view', },
        { label: 'subscriptions_aliases', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
aliasName,
auto_renew,
beneficiary,
beneficiary_tenant_id,
billingAccountName,
billing_frequency,
billing_policies,
billing_profile_display_name,
billing_profile_id,
billing_profile_name,
billing_subscription_id,
consumption_cost_center,
customer_display_name,
customer_id,
customer_name,
display_name,
enrollment_account_display_name,
enrollment_account_id,
enrollment_account_subscription_details,
invoice_section_display_name,
invoice_section_id,
invoice_section_name,
last_month_charges,
month_to_date_charges,
next_billing_cycle_details,
offer_id,
operation_status,
product_category,
product_type,
product_type_id,
provisioning_state,
provisioning_tenant_id,
purchase_date,
quantity,
renewal_term_details,
reseller,
resource_uri,
sku_description,
sku_id,
status,
subscription_id,
suspension_reason_details,
suspension_reasons,
system_overrides,
tags,
term_duration,
term_end_date,
term_start_date
FROM azure.billing.vw_subscriptions_aliases
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.subscriptions_aliases
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscriptions_aliases</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.billing.subscriptions_aliases (
aliasName,
billingAccountName,
tags,
properties
)
SELECT 
'{{ aliasName }}',
'{{ billingAccountName }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: properties
      value:
        - name: autoRenew
          value: string
        - name: beneficiaryTenantId
          value: string
        - name: beneficiary
          value:
            - name: tenantId
              value: string
            - name: objectId
              value: string
        - name: billingFrequency
          value: string
        - name: billingProfileId
          value: string
        - name: billingPolicies
          value: object
        - name: billingProfileDisplayName
          value: string
        - name: billingProfileName
          value: string
        - name: consumptionCostCenter
          value: string
        - name: customerId
          value: string
        - name: customerDisplayName
          value: string
        - name: customerName
          value: string
        - name: displayName
          value: string
        - name: enrollmentAccountId
          value: string
        - name: enrollmentAccountDisplayName
          value: string
        - name: enrollmentAccountSubscriptionDetails
          value:
            - name: enrollmentAccountStartDate
              value: string
            - name: subscriptionEnrollmentAccountStatus
              value: string
        - name: invoiceSectionId
          value: string
        - name: invoiceSectionDisplayName
          value: string
        - name: invoiceSectionName
          value: string
        - name: lastMonthCharges
          value:
            - name: currency
              value: string
            - name: value
              value: number
        - name: nextBillingCycleDetails
          value:
            - name: billingFrequency
              value: string
        - name: offerId
          value: string
        - name: productCategory
          value: string
        - name: productType
          value: string
        - name: productTypeId
          value: string
        - name: purchaseDate
          value: string
        - name: quantity
          value: integer
        - name: reseller
          value:
            - name: resellerId
              value: string
            - name: description
              value: string
        - name: renewalTermDetails
          value:
            - name: billingFrequency
              value: string
            - name: productId
              value: string
            - name: productTypeId
              value: string
            - name: skuId
              value: string
            - name: termDuration
              value: string
            - name: quantity
              value: integer
            - name: termEndDate
              value: string
        - name: skuId
          value: string
        - name: skuDescription
          value: string
        - name: systemOverrides
          value:
            - name: cancellation
              value: string
            - name: cancellationAllowedEndDate
              value: string
        - name: resourceUri
          value: string
        - name: termDuration
          value: string
        - name: termStartDate
          value: string
        - name: termEndDate
          value: string
        - name: provisioningTenantId
          value: string
        - name: status
          value: string
        - name: operationStatus
          value: string
        - name: provisioningState
          value: string
        - name: subscriptionId
          value: string
        - name: suspensionReasons
          value:
            - string
        - name: suspensionReasonDetails
          value:
            - - name: effectiveDate
                value: string
              - name: reason
                value: string
        - name: billingSubscriptionId
          value: string

```
</TabItem>
</Tabs>
