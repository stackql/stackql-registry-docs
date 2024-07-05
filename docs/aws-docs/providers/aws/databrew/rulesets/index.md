---
title: rulesets
hide_title: false
hide_table_of_contents: false
keywords:
  - rulesets
  - databrew
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

Creates, updates, deletes or gets a <code>ruleset</code> resource or lists <code>rulesets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>rulesets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataBrew::Ruleset.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.databrew.rulesets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the Ruleset</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the Ruleset</td></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td>Arn of the target resource (dataset) to apply the ruleset to</td></tr>
<tr><td><CopyableCode code="rules" /></td><td><code>array</code></td><td>List of the data quality rules in the ruleset</td></tr>
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
    <td><CopyableCode code="Name, TargetArn, Rules, region" /></td>
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
Gets all <code>rulesets</code> in a region.
```sql
SELECT
region,
name,
description,
target_arn,
rules,
tags
FROM aws.databrew.rulesets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ruleset</code>.
```sql
SELECT
region,
name,
description,
target_arn,
rules,
tags
FROM aws.databrew.rulesets
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ruleset</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.databrew.rulesets (
 Name,
 TargetArn,
 Rules,
 region
)
SELECT 
'{{ Name }}',
 '{{ TargetArn }}',
 '{{ Rules }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.databrew.rulesets (
 Name,
 Description,
 TargetArn,
 Rules,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ TargetArn }}',
 '{{ Rules }}',
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
  - name: ruleset
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: TargetArn
        value: '{{ TargetArn }}'
      - name: Rules
        value:
          - Name: '{{ Name }}'
            Disabled: '{{ Disabled }}'
            CheckExpression: '{{ CheckExpression }}'
            SubstitutionMap:
              - ValueReference: '{{ ValueReference }}'
                Value: '{{ Value }}'
            Threshold:
              Value: null
              Type: '{{ Type }}'
              Unit: '{{ Unit }}'
            ColumnSelectors:
              - Regex: '{{ Regex }}'
                Name: '{{ Name }}'
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
DELETE FROM aws.databrew.rulesets
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>rulesets</code> resource, the following permissions are required:

### Create
```json
databrew:CreateRuleset,
databrew:TagResource,
databrew:UntagResource,
iam:PassRole
```

### Read
```json
databrew:DescribeRuleset,
databrew:ListTagsForResource,
iam:ListRoles
```

### Update
```json
databrew:UpdateRuleset
```

### Delete
```json
databrew:DeleteRuleset
```

### List
```json
databrew:ListRulesets,
databrew:ListTagsForResource,
iam:ListRoles
```

