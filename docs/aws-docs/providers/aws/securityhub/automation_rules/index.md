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


Used to retrieve a list of <code>automation_rules</code> in a region or to create or delete a <code>automation_rules</code> resource, use <code>automation_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>automation_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SecurityHub::AutomationRule`` resource specifies an automation rule based on input parameters. For more information, see &#91;Automation rules&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;latest&#x2F;userguide&#x2F;automation-rules.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.automation_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
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
rule_arn
FROM aws.securityhub.automation_rules
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>automation_rule</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- automation_rule.iql (required properties only)
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
-- automation_rule.iql (all properties)
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

## `DELETE` Example

```sql
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

