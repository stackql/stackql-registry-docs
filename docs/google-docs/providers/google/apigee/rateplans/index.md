---
title: rateplans
hide_title: false
hide_table_of_contents: false
keywords:
  - rateplans
  - apigee
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

Creates, updates, deletes, gets or lists a <code>rateplans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rateplans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.rateplans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the rate plan. |
| <CopyableCode code="description" /> | `string` | Description of the rate plan. |
| <CopyableCode code="apiproduct" /> | `string` | Name of the API product that the rate plan is associated with. |
| <CopyableCode code="billingPeriod" /> | `string` | Frequency at which the customer will be billed. |
| <CopyableCode code="consumptionPricingRates" /> | `array` | API call volume ranges and the fees charged when the total number of API calls is within a given range. The method used to calculate the final fee depends on the selected pricing model. For example, if the pricing model is `STAIRSTEP` and the ranges are defined as follows: ``` { "start": 1, "end": 100, "fee": 75 }, { "start": 101, "end": 200, "fee": 100 }, } ``` Then the following fees would be charged based on the total number of API calls (assuming the currency selected is `USD`): * 1 call costs $75 * 50 calls cost $75 * 150 calls cost $100 The number of API calls cannot exceed 200. |
| <CopyableCode code="consumptionPricingType" /> | `string` | Pricing model used for consumption-based charges. |
| <CopyableCode code="createdAt" /> | `string` | Output only. Time that the rate plan was created in milliseconds since epoch. |
| <CopyableCode code="currencyCode" /> | `string` | Currency to be used for billing. Consists of a three-letter code as defined by the [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) standard. |
| <CopyableCode code="displayName" /> | `string` | Display name of the rate plan. |
| <CopyableCode code="endTime" /> | `string` | Time when the rate plan will expire in milliseconds since epoch. Set to 0 or `null` to indicate that the rate plan should never expire. |
| <CopyableCode code="fixedFeeFrequency" /> | `integer` | Frequency at which the fixed fee is charged. |
| <CopyableCode code="fixedRecurringFee" /> | `object` | Represents an amount of money with its currency type. |
| <CopyableCode code="lastModifiedAt" /> | `string` | Output only. Time the rate plan was last modified in milliseconds since epoch. |
| <CopyableCode code="paymentFundingModel" /> | `string` | DEPRECATED: This field is no longer supported and will eventually be removed when Apigee Hybrid 1.5/1.6 is no longer supported. Instead, use the `billingType` field inside `DeveloperMonetizationConfig` resource. Flag that specifies the billing account type, prepaid or postpaid. |
| <CopyableCode code="revenueShareRates" /> | `array` | Details of the revenue sharing model. |
| <CopyableCode code="revenueShareType" /> | `string` | Method used to calculate the revenue that is shared with developers. |
| <CopyableCode code="setupFee" /> | `object` | Represents an amount of money with its currency type. |
| <CopyableCode code="startTime" /> | `string` | Time when the rate plan becomes active in milliseconds since epoch. |
| <CopyableCode code="state" /> | `string` | Current state of the rate plan (draft or published). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_apiproducts_rateplans_get" /> | `SELECT` | <CopyableCode code="apiproductsId, organizationsId, rateplansId" /> | Gets the details of a rate plan. |
| <CopyableCode code="organizations_apiproducts_rateplans_list" /> | `SELECT` | <CopyableCode code="apiproductsId, organizationsId" /> | Lists all the rate plans for an API product. |
| <CopyableCode code="organizations_apiproducts_rateplans_create" /> | `INSERT` | <CopyableCode code="apiproductsId, organizationsId" /> | Create a rate plan that is associated with an API product in an organization. Using rate plans, API product owners can monetize their API products by configuring one or more of the following: - Billing frequency - Initial setup fees for using an API product - Payment funding model (postpaid only) - Fixed recurring or consumption-based charges for using an API product - Revenue sharing with developer partners An API product can have multiple rate plans associated with it but *only one* rate plan can be active at any point of time. **Note: From the developer's perspective, they purchase API products not rate plans. |
| <CopyableCode code="organizations_apiproducts_rateplans_delete" /> | `DELETE` | <CopyableCode code="apiproductsId, organizationsId, rateplansId" /> | Deletes a rate plan. |
| <CopyableCode code="organizations_apiproducts_rateplans_update" /> | `REPLACE` | <CopyableCode code="apiproductsId, organizationsId, rateplansId" /> | Updates an existing rate plan. |

## `SELECT` examples

Lists all the rate plans for an API product.

```sql
SELECT
name,
description,
apiproduct,
billingPeriod,
consumptionPricingRates,
consumptionPricingType,
createdAt,
currencyCode,
displayName,
endTime,
fixedFeeFrequency,
fixedRecurringFee,
lastModifiedAt,
paymentFundingModel,
revenueShareRates,
revenueShareType,
setupFee,
startTime,
state
FROM google.apigee.rateplans
WHERE apiproductsId = '{{ apiproductsId }}'
AND organizationsId = '{{ organizationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>rateplans</code> resource.

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
INSERT INTO google.apigee.rateplans (
apiproductsId,
organizationsId,
fixedFeeFrequency,
description,
consumptionPricingRates,
revenueShareType,
apiproduct,
state,
consumptionPricingType,
billingPeriod,
revenueShareRates,
startTime,
currencyCode,
paymentFundingModel,
endTime,
setupFee,
fixedRecurringFee,
displayName
)
SELECT 
'{{ apiproductsId }}',
'{{ organizationsId }}',
'{{ fixedFeeFrequency }}',
'{{ description }}',
'{{ consumptionPricingRates }}',
'{{ revenueShareType }}',
'{{ apiproduct }}',
'{{ state }}',
'{{ consumptionPricingType }}',
'{{ billingPeriod }}',
'{{ revenueShareRates }}',
'{{ startTime }}',
'{{ currencyCode }}',
'{{ paymentFundingModel }}',
'{{ endTime }}',
'{{ setupFee }}',
'{{ fixedRecurringFee }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: fixedFeeFrequency
      value: integer
    - name: name
      value: string
    - name: description
      value: string
    - name: consumptionPricingRates
      value:
        - - name: fee
            value:
              - name: units
                value: string
              - name: currencyCode
                value: string
              - name: nanos
                value: integer
          - name: end
            value: string
          - name: start
            value: string
    - name: revenueShareType
      value: string
    - name: apiproduct
      value: string
    - name: state
      value: string
    - name: consumptionPricingType
      value: string
    - name: billingPeriod
      value: string
    - name: revenueShareRates
      value:
        - - name: end
            value: string
          - name: start
            value: string
          - name: sharePercentage
            value: number
    - name: startTime
      value: string
    - name: currencyCode
      value: string
    - name: paymentFundingModel
      value: string
    - name: endTime
      value: string
    - name: lastModifiedAt
      value: string
    - name: createdAt
      value: string
    - name: displayName
      value: string

```
</TabItem>
</Tabs>

## `REPLACE` example

Replaces all fields in the specified <code>rateplans</code> resource.

```sql
/*+ update */
REPLACE google.apigee.rateplans
SET 
fixedFeeFrequency = '{{ fixedFeeFrequency }}',
description = '{{ description }}',
consumptionPricingRates = '{{ consumptionPricingRates }}',
revenueShareType = '{{ revenueShareType }}',
apiproduct = '{{ apiproduct }}',
state = '{{ state }}',
consumptionPricingType = '{{ consumptionPricingType }}',
billingPeriod = '{{ billingPeriod }}',
revenueShareRates = '{{ revenueShareRates }}',
startTime = '{{ startTime }}',
currencyCode = '{{ currencyCode }}',
paymentFundingModel = '{{ paymentFundingModel }}',
endTime = '{{ endTime }}',
setupFee = '{{ setupFee }}',
fixedRecurringFee = '{{ fixedRecurringFee }}',
displayName = '{{ displayName }}'
WHERE 
apiproductsId = '{{ apiproductsId }}'
AND organizationsId = '{{ organizationsId }}'
AND rateplansId = '{{ rateplansId }}';
```

## `DELETE` example

Deletes the specified <code>rateplans</code> resource.

```sql
/*+ delete */
DELETE FROM google.apigee.rateplans
WHERE apiproductsId = '{{ apiproductsId }}'
AND organizationsId = '{{ organizationsId }}'
AND rateplansId = '{{ rateplansId }}';
```
