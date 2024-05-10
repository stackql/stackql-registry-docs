---
title: pricing_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - pricing_rules
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


Used to retrieve a list of <code>pricing_rules</code> in a region or to create or delete a <code>pricing_rules</code> resource, use <code>pricing_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pricing_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A markup&#x2F;discount that is defined for a specific set of services that can later be associated with a pricing plan.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.billingconductor.pricing_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Pricing rule ARN</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
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
FROM aws.billingconductor.pricing_rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>pricing_rule</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- pricing_rule.iql (required properties only)
INSERT INTO aws.billingconductor.pricing_rules (
 Name,
 Scope,
 Type,
 region
)
SELECT 
'{{ Name }}',
 '{{ Scope }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- pricing_rule.iql (all properties)
INSERT INTO aws.billingconductor.pricing_rules (
 Name,
 Description,
 Scope,
 Type,
 ModifierPercentage,
 Service,
 BillingEntity,
 Tiering,
 UsageType,
 Operation,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Scope }}',
 '{{ Type }}',
 '{{ ModifierPercentage }}',
 '{{ Service }}',
 '{{ BillingEntity }}',
 '{{ Tiering }}',
 '{{ UsageType }}',
 '{{ Operation }}',
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
  - name: pricing_rule
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Scope
        value: '{{ Scope }}'
      - name: Type
        value: '{{ Type }}'
      - name: ModifierPercentage
        value: null
      - name: Service
        value: '{{ Service }}'
      - name: BillingEntity
        value: '{{ BillingEntity }}'
      - name: Tiering
        value:
          FreeTier:
            Activated: '{{ Activated }}'
      - name: UsageType
        value: '{{ UsageType }}'
      - name: Operation
        value: '{{ Operation }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.billingconductor.pricing_rules
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>pricing_rules</code> resource, the following permissions are required:

### Create
```json
billingconductor:CreatePricingRule,
billingconductor:ListPricingRules,
billingconductor:TagResource,
billingconductor:ListTagsForResource
```

### Delete
```json
billingconductor:DeletePricingRule,
billingconductor:ListPricingRules,
billingconductor:UntagResource
```

### List
```json
billingconductor:ListPricingRules,
billingconductor:ListTagsForResource
```

