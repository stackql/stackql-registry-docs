---
title: automation_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - automation_rules
  - securityhub
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

Creates, updates, deletes or gets an <code>automation_rule</code> resource or lists <code>automation_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automation_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SecurityHub::AutomationRule</code> resource specifies an automation rule based on input parameters. For more information, see &#91;Automation rules&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/automation-rules.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.automation_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_status" /></td><td><code>string</code></td><td>Whether the rule is active after it is created. If this parameter is equal to <code>ENABLED</code>, ASH applies the rule to findings and finding updates after the rule is created.</td></tr>
<tr><td><CopyableCode code="rule_order" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="rule_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>The date and time, in UTC and ISO 8601 format.</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>The date and time, in UTC and ISO 8601 format.</code></td><td></td></tr>
<tr><td><CopyableCode code="created_by" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="is_terminal" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="criteria" /></td><td><code>object</code></td><td>A set of &#91;Security Finding Format (ASFF)&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-findings-format.html) finding field attributes and corresponding expected values that ASH uses to filter findings. If a rule is enabled and a finding matches the criteria specified in this parameter, ASH applies the rule action to the finding.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>A key-value pair to associate with a resource.</code></td><td></td></tr>
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
    <td><CopyableCode code="region" /></td>
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
List all <code>automation_rules</code> in a region.
```sql
SELECT
region,
rule_arn
FROM aws.securityhub.automation_rules
WHERE region = 'us-east-1';
```
Gets all properties from an <code>automation_rule</code>.
```sql
SELECT
region,
rule_arn,
rule_status,
rule_order,
description,
rule_name,
created_at,
updated_at,
created_by,
is_terminal,
actions,
criteria,
tags
FROM aws.securityhub.automation_rules
WHERE region = 'us-east-1' AND data__Identifier = '<RuleArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>automation_rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.automation_rules (
 RuleStatus,
 RuleOrder,
 Description,
 RuleName,
 IsTerminal,
 Actions,
 Criteria,
 Tags,
 region
)
SELECT 
'{{ RuleStatus }}',
 '{{ RuleOrder }}',
 '{{ Description }}',
 '{{ RuleName }}',
 '{{ IsTerminal }}',
 '{{ Actions }}',
 '{{ Criteria }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.automation_rules (
 RuleStatus,
 RuleOrder,
 Description,
 RuleName,
 IsTerminal,
 Actions,
 Criteria,
 Tags,
 region
)
SELECT 
 '{{ RuleStatus }}',
 '{{ RuleOrder }}',
 '{{ Description }}',
 '{{ RuleName }}',
 '{{ IsTerminal }}',
 '{{ Actions }}',
 '{{ Criteria }}',
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
  - name: automation_rule
    props:
      - name: RuleStatus
        value: '{{ RuleStatus }}'
      - name: RuleOrder
        value: '{{ RuleOrder }}'
      - name: Description
        value: '{{ Description }}'
      - name: RuleName
        value: '{{ RuleName }}'
      - name: IsTerminal
        value: '{{ IsTerminal }}'
      - name: Actions
        value:
          - Type: '{{ Type }}'
            FindingFieldsUpdate:
              Types:
                - '{{ Types[0] }}'
              Severity:
                Product: null
                Label: '{{ Label }}'
                Normalized: '{{ Normalized }}'
              Confidence: null
              Criticality: null
              UserDefinedFields: {}
              VerificationState: '{{ VerificationState }}'
              RelatedFindings:
                - ProductArn: '{{ ProductArn }}'
                  Id: null
              Note:
                Text: '{{ Text }}'
                UpdatedBy: null
              Workflow:
                Status: '{{ Status }}'
      - name: Criteria
        value:
          ProductArn:
            - Comparison: '{{ Comparison }}'
              Value: '{{ Value }}'
          AwsAccountId:
            - null
          Id:
            - null
          GeneratorId:
            - null
          Type:
            - null
          FirstObservedAt:
            - DateRange:
                Unit: '{{ Unit }}'
                Value: null
              End: '{{ End }}'
              Start: null
          LastObservedAt:
            - null
          CreatedAt:
            - null
          UpdatedAt:
            - null
          Confidence:
            - Eq: null
              Gte: null
              Lte: null
          Criticality:
            - null
          Title:
            - null
          Description:
            - null
          SourceUrl:
            - null
          ProductName:
            - null
          CompanyName:
            - null
          SeverityLabel:
            - null
          ResourceType:
            - null
          ResourceId:
            - null
          ResourcePartition:
            - null
          ResourceRegion:
            - null
          ResourceTags:
            - Comparison: '{{ Comparison }}'
              Key: null
              Value: null
          ResourceDetailsOther:
            - null
          ComplianceStatus:
            - null
          ComplianceSecurityControlId:
            - null
          ComplianceAssociatedStandardsId:
            - null
          VerificationState:
            - null
          WorkflowStatus:
            - null
          RecordState:
            - null
          RelatedFindingsProductArn:
            - null
          RelatedFindingsId:
            - null
          NoteText:
            - null
          NoteUpdatedAt:
            - null
          NoteUpdatedBy:
            - null
          UserDefinedFields:
            - null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.automation_rules
WHERE data__Identifier = '<RuleArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>automation_rules</code> resource, the following permissions are required:

### Create
```json
securityhub:CreateAutomationRule,
securityhub:TagResource,
securityhub:ListTagsForResource
```

### Read
```json
securityhub:ListAutomationRules,
securityhub:BatchGetAutomationRules,
securityhub:ListTagsForResource
```

### Update
```json
securityhub:BatchUpdateAutomationRules,
securityhub:TagResource,
securityhub:UntagResource,
securityhub:ListTagsForResource
```

### Delete
```json
securityhub:BatchDeleteAutomationRules,
securityhub:BatchGetAutomationRules
```

### List
```json
securityhub:ListAutomationRules,
securityhub:ListTagsForResource
```

