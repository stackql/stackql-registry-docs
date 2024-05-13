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


Used to retrieve a list of <code>custom_line_items</code> in a region or to create or delete a <code>custom_line_items</code> resource, use <code>custom_line_item</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_line_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A custom line item is an one time charge that is applied to a specific billing group's bill.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.custom_line_items" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.billingconductor.custom_line_items
WHERE region = 'us-east-1';
```

## `INSERT` Example

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

## `DELETE` Example

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

### List
```json
billingconductor:ListCustomLineItems,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:ListTagsForResource
```

### Delete
```json
billingconductor:DeleteCustomLineItem,
billingconductor:ListCustomLineItems,
billingconductor:BatchDisassociateResourcesFromCustomLineItem,
billingconductor:ListResourcesAssociatedToCustomLineItem,
billingconductor:UntagResource
```

