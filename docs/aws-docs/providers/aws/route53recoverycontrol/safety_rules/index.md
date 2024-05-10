---
title: safety_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - safety_rules
  - route53recoverycontrol
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


Used to retrieve a list of <code>safety_rules</code> in a region or to create or delete a <code>safety_rules</code> resource, use <code>safety_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>safety_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.safety_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="safety_rule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the safety rule.</td></tr>
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
safety_rule_arn
FROM aws.route53recoverycontrol.safety_rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>safety_rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- safety_rule.iql (required properties only)
INSERT INTO aws.route53recoverycontrol.safety_rules (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- safety_rule.iql (all properties)
INSERT INTO aws.route53recoverycontrol.safety_rules (
 AssertionRule,
 GatingRule,
 Name,
 ControlPanelArn,
 RuleConfig,
 Tags,
 region
)
SELECT 
 '{{ AssertionRule }}',
 '{{ GatingRule }}',
 '{{ Name }}',
 '{{ ControlPanelArn }}',
 '{{ RuleConfig }}',
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
  - name: safety_rule
    props:
      - name: AssertionRule
        value:
          WaitPeriodMs: '{{ WaitPeriodMs }}'
          AssertedControls:
            - '{{ AssertedControls[0] }}'
      - name: GatingRule
        value:
          GatingControls:
            - '{{ GatingControls[0] }}'
          TargetControls:
            - '{{ TargetControls[0] }}'
          WaitPeriodMs: '{{ WaitPeriodMs }}'
      - name: Name
        value: '{{ Name }}'
      - name: ControlPanelArn
        value: '{{ ControlPanelArn }}'
      - name: RuleConfig
        value:
          Type: '{{ Type }}'
          Threshold: '{{ Threshold }}'
          Inverted: '{{ Inverted }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53recoverycontrol.safety_rules
WHERE data__Identifier = '<SafetyRuleArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>safety_rules</code> resource, the following permissions are required:

### Create
```json
route53-recovery-control-config:CreateSafetyRule,
route53-recovery-control-config:DescribeSafetyRule,
route53-recovery-control-config:DescribeControlPanel,
route53-recovery-control-config:DescribeRoutingControl,
route53-recovery-control-config:ListTagsForResource,
route53-recovery-control-config:TagResource
```

### Delete
```json
route53-recovery-control-config:DescribeSafetyRule,
route53-recovery-control-config:DeleteSafetyRule
```

### List
```json
route53-recovery-control-config:ListSafetyRules
```

