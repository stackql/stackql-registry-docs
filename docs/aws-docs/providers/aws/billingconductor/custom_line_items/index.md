---
title: custom_line_items
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_line_items
  - billingconductor
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>custom_line_item</code> resource or lists <code>custom_line_items</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_line_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A custom line item is an one time charge that is applied to a specific billing group's bill.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.custom_line_items" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_line_item_charge_details" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="billing_group_arn" /></td><td><code>string</code></td><td>Billing Group ARN</td></tr>
<tr><td><CopyableCode code="billing_period_range" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>integer</code></td><td>Creation timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="last_modified_time" /></td><td><code>integer</code></td><td>Latest modified timestamp in UNIX epoch time format</td></tr>
<tr><td><CopyableCode code="association_size" /></td><td><code>integer</code></td><td>Number of source values associated to this custom line item</td></tr>
<tr><td><CopyableCode code="product_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="currency_code" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>The account which this custom line item will be charged to</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, BillingGroupArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>custom_line_items</code> in a region.
```sql
SELECT
region,
arn
FROM aws.billingconductor.custom_line_items
WHERE region = 'us-east-1';
```
Gets all properties from a <code>custom_line_item</code>.
```sql
SELECT
region,
name,
description,
custom_line_item_charge_details,
billing_group_arn,
billing_period_range,
arn,
creation_time,
last_modified_time,
association_size,
product_code,
currency_code,
account_id,
tags
FROM aws.billingconductor.custom_line_items
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_line_item</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.billingconductor.custom_line_items (
 Name,
 BillingGroupArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ BillingGroupArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.billingconductor.custom_line_items (
 Name,
 Description,
 CustomLineItemChargeDetails,
 BillingGroupArn,
 BillingPeriodRange,
 AccountId,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ CustomLineItemChargeDetails }}',
 '{{ BillingGroupArn }}',
 '{{ BillingPeriodRange }}',
 '{{ AccountId }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: custom_line_item
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: CustomLineItemChargeDetails
        value:
          Flat:
            ChargeValue: null
          Percentage:
            ChildAssociatedResources:
              - '{{ ChildAssociatedResources[0] }}'
            PercentageValue: null
          Type: '{{ Type }}'
          LineItemFilters:
            - Attribute: '{{ Attribute }}'
              MatchOption: '{{ MatchOption }}'
              Values:
                - '{{ Values[0] }}'
      - name: BillingGroupArn
        value: '{{ BillingGroupArn }}'
      - name: BillingPeriodRange
        value:
          InclusiveStartBillingPeriod: '{{ InclusiveStartBillingPeriod }}'
          ExclusiveEndBillingPeriod: '{{ ExclusiveEndBillingPeriod }}'
      - name: AccountId
        value: '{{ AccountId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.billingconductor.custom_line_items
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>custom_line_items</code> resource, the following permissions are required:

### Create
```json
billingconductor:CreateCustomLineItem,
billingconductor:BatchAssociateResourcesToCustomLineItem,
billingconductor:ListCustomLineItems,
billingconductor:TagResource,
billingconductor:ListTagsForResource
```

### Read
```json
billingconductor:ListCustomLineItems,
billingconductor:ListCustomLineItemVersions,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:ListTagsForResource
```

### List
```json
billingconductor:ListCustomLineItems,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:ListTagsForResource
```

### Update
```json
billingconductor:UpdateCustomLineItem,
billingconductor:ListCustomLineItems,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:BatchAssociateResourcesToCustomLineItem,
billingconductor:BatchDisassociateResourcesFromCustomLineItem,
billingconductor:TagResource,
billingconductor:UntagResource
```

### Delete
```json
billingconductor:DeleteCustomLineItem,
billingconductor:ListCustomLineItems,
billingconductor:BatchDisassociateResourcesFromCustomLineItem,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:UntagResource
```

