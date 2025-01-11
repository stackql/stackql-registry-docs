---
title: cost_categories
hide_title: false
hide_table_of_contents: false
keywords:
  - cost_categories
  - ce
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

Creates, updates, deletes or gets a <code>cost_category</code> resource or lists <code>cost_categories</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cost_categories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Cost Category enables you to map your cost and usage into meaningful categories. You can use Cost Category to organize your costs using a rule-based engine.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ce.cost_categories" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Cost category ARN</td></tr>
<tr><td><CopyableCode code="effective_start" /></td><td><code>string</code></td><td>ISO 8601 date time with offset format</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rules" /></td><td><code>string</code></td><td>JSON array format of Expression in Billing and Cost Management API</td></tr>
<tr><td><CopyableCode code="split_charge_rules" /></td><td><code>string</code></td><td>Json array format of CostCategorySplitChargeRule in Billing and Cost Management API</td></tr>
<tr><td><CopyableCode code="default_value" /></td><td><code>string</code></td><td>The default value for the cost category</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ce-costcategory.html"><code>AWS::CE::CostCategory</code></a>.

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
    <td><CopyableCode code="Name, RuleVersion, Rules, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>cost_categories</code> in a region.
```sql
SELECT
region,
arn,
effective_start,
name,
rule_version,
rules,
split_charge_rules,
default_value
FROM aws.ce.cost_categories
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>cost_category</code>.
```sql
SELECT
region,
arn,
effective_start,
name,
rule_version,
rules,
split_charge_rules,
default_value
FROM aws.ce.cost_categories
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cost_category</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ce.cost_categories (
 Name,
 RuleVersion,
 Rules,
 region
)
SELECT 
'{{ Name }}',
 '{{ RuleVersion }}',
 '{{ Rules }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ce.cost_categories (
 Name,
 RuleVersion,
 Rules,
 SplitChargeRules,
 DefaultValue,
 region
)
SELECT 
 '{{ Name }}',
 '{{ RuleVersion }}',
 '{{ Rules }}',
 '{{ SplitChargeRules }}',
 '{{ DefaultValue }}',
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
  - name: cost_category
    props:
      - name: Name
        value: '{{ Name }}'
      - name: RuleVersion
        value: '{{ RuleVersion }}'
      - name: Rules
        value: '{{ Rules }}'
      - name: SplitChargeRules
        value: '{{ SplitChargeRules }}'
      - name: DefaultValue
        value: '{{ DefaultValue }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ce.cost_categories
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cost_categories</code> resource, the following permissions are required:

### Create
```json
ce:CreateCostCategoryDefinition
```

### Read
```json
ce:DescribeCostCategoryDefinition
```

### Update
```json
ce:UpdateCostCategoryDefinition
```

### Delete
```json
ce:DeleteCostCategoryDefinition
```

### List
```json
ce:ListCostCategoryDefinitions
```
