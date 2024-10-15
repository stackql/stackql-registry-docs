---
title: profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - profiles
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

Creates, updates, deletes, gets or lists a <code>profiles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.profiles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="bill_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingAccountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billingProfileName" /> | `text` | field from the `properties` object |
| <CopyableCode code="billing_relationship_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="currency" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_payment_term" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled_azure_plans" /> | `text` | field from the `properties` object |
| <CopyableCode code="has_read_access" /> | `text` | field from the `properties` object |
| <CopyableCode code="indirect_relationship_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_day" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_email_opt_in" /> | `text` | field from the `properties` object |
| <CopyableCode code="invoice_recipients" /> | `text` | field from the `properties` object |
| <CopyableCode code="other_payment_terms" /> | `text` | field from the `properties` object |
| <CopyableCode code="po_number" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="ship_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="sold_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="spending_limit" /> | `text` | field from the `properties` object |
| <CopyableCode code="spending_limit_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_reason_code" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
| <CopyableCode code="target_clouds" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A billing profile. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Gets a billing profile by its ID. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | Lists the billing profiles that a user has access to. The operation is supported for billing accounts with agreement of type Microsoft Customer Agreement and Microsoft Partner Agreement. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName" /> | Creates or updates a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. If you are a MCA Individual (Pay-as-you-go) customer, then please use the Azure portal experience to create the billing profile. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="billingAccountName, billingProfileName" /> | Deletes a billing profile. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. |
| <CopyableCode code="validate_delete_eligibility" /> | `EXEC` | <CopyableCode code="billingAccountName, billingProfileName" /> | Validates if the billing profile can be deleted. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement and Microsoft Partner Agreement. |

## `SELECT` examples

Lists the billing profiles that a user has access to. The operation is supported for billing accounts with agreement of type Microsoft Customer Agreement and Microsoft Partner Agreement.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_profiles', value: 'view', },
        { label: 'profiles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
bill_to,
billingAccountName,
billingProfileName,
billing_relationship_type,
currency,
current_payment_term,
display_name,
enabled_azure_plans,
has_read_access,
indirect_relationship_info,
invoice_day,
invoice_email_opt_in,
invoice_recipients,
other_payment_terms,
po_number,
provisioning_state,
ship_to,
sold_to,
spending_limit,
spending_limit_details,
status,
status_reason_code,
system_id,
tags,
target_clouds
FROM azure.billing.vw_profiles
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
tags
FROM azure.billing.profiles
WHERE billingAccountName = '{{ billingAccountName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>profiles</code> resource.

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
INSERT INTO azure.billing.profiles (
billingAccountName,
billingProfileName,
tags,
properties
)
SELECT 
'{{ billingAccountName }}',
'{{ billingProfileName }}',
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
        - name: provisioningState
          value: string
        - name: billingRelationshipType
          value: string
        - name: billTo
          value: string
        - name: currency
          value: string
        - name: displayName
          value: string
        - name: enabledAzurePlans
          value:
            - - name: productId
                value: string
              - name: skuId
                value: string
              - name: skuDescription
                value: string
        - name: hasReadAccess
          value: boolean
        - name: indirectRelationshipInfo
          value: string
        - name: invoiceDay
          value: integer
        - name: invoiceEmailOptIn
          value: boolean
        - name: invoiceRecipients
          value:
            - string
        - name: poNumber
          value: string
        - name: shipTo
          value: string
        - name: soldTo
          value: string
        - name: spendingLimit
          value: string
        - name: spendingLimitDetails
          value:
            - - name: amount
                value: number
              - name: currency
                value: string
              - name: startDate
                value: string
              - name: endDate
                value: string
              - name: type
                value: string
              - name: status
                value: string
        - name: status
          value: string
        - name: statusReasonCode
          value: string
        - name: systemId
          value: string
        - name: tags
          value: object
        - name: targetClouds
          value:
            - string
        - name: currentPaymentTerm
          value: string
        - name: otherPaymentTerms
          value:
            - - name: term
                value: string
              - name: startDate
                value: string
              - name: endDate
                value: string
              - name: isDefault
                value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>profiles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.billing.profiles
WHERE billingAccountName = '{{ billingAccountName }}'
AND billingProfileName = '{{ billingProfileName }}';
```
