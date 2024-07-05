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

Creates, updates, deletes or gets a <code>safety_rule</code> resource or lists <code>safety_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>safety_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS Route53 Recovery Control basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53recoverycontrol.safety_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="assertion_rule" /></td><td><code>object</code></td><td>An assertion rule enforces that, when a routing control state is changed, that the criteria set by the rule configuration is met. Otherwise, the change to the routing control is not accepted.</td></tr>
<tr><td><CopyableCode code="gating_rule" /></td><td><code>object</code></td><td>A gating rule verifies that a set of gating controls evaluates as true, based on a rule configuration that you specify. If the gating rule evaluates to true, Amazon Route 53 Application Recovery Controller allows a set of routing control state changes to run and complete against the set of target controls.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name for the safety rule.</td></tr>
<tr><td><CopyableCode code="safety_rule_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the safety rule.</td></tr>
<tr><td><CopyableCode code="control_panel_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the control panel.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The deployment status of the routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="rule_config" /></td><td><code>object</code></td><td>The rule configuration for an assertion rule or gating rule. This is the criteria that you set for specific assertion controls (routing controls) or gating controls. This configuration specifies how many controls must be enabled after a transaction completes.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>safety_rules</code> in a region.
```sql
SELECT
region,
assertion_rule,
gating_rule,
name,
safety_rule_arn,
control_panel_arn,
status,
rule_config,
tags
FROM aws.route53recoverycontrol.safety_rules
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>safety_rule</code>.
```sql
SELECT
region,
assertion_rule,
gating_rule,
name,
safety_rule_arn,
control_panel_arn,
status,
rule_config,
tags
FROM aws.route53recoverycontrol.safety_rules
WHERE region = 'us-east-1' AND data__Identifier = '<SafetyRuleArn>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
route53-recovery-control-config:DescribeSafetyRule,
route53-recovery-control-config:ListTagsForResource
```

### Update
```json
route53-recovery-control-config:UpdateSafetyRule,
route53-recovery-control-config:DescribeSafetyRule,
route53-recovery-control-config:ListTagsForResource,
route53-recovery-control-config:TagResource,
route53-recovery-control-config:UntagResource
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

