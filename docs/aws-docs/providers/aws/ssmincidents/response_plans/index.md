---
title: response_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - response_plans
  - ssmincidents
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


Used to retrieve a list of <code>response_plans</code> in a region or to create or delete a <code>response_plans</code> resource, use <code>response_plan</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ResponsePlan</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.response_plans" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the response plan.</td></tr>
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
    <td><CopyableCode code="Name, IncidentTemplate, region" /></td>
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
FROM aws.ssmincidents.response_plans
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>response_plan</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ssmincidents.response_plans (
 Name,
 IncidentTemplate,
 region
)
SELECT 
'{{ Name }}',
 '{{ IncidentTemplate }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssmincidents.response_plans (
 Name,
 DisplayName,
 ChatChannel,
 Engagements,
 Actions,
 Integrations,
 Tags,
 IncidentTemplate,
 region
)
SELECT 
 '{{ Name }}',
 '{{ DisplayName }}',
 '{{ ChatChannel }}',
 '{{ Engagements }}',
 '{{ Actions }}',
 '{{ Integrations }}',
 '{{ Tags }}',
 '{{ IncidentTemplate }}',
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
  - name: response_plan
    props:
      - name: Name
        value: '{{ Name }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: ChatChannel
        value:
          ChatbotSns:
            - '{{ ChatbotSns[0] }}'
      - name: Engagements
        value:
          - '{{ Engagements[0] }}'
      - name: Actions
        value:
          - SsmAutomation:
              RoleArn: '{{ RoleArn }}'
              DocumentName: '{{ DocumentName }}'
              DocumentVersion: '{{ DocumentVersion }}'
              TargetAccount: '{{ TargetAccount }}'
              Parameters:
                - Key: '{{ Key }}'
                  Values:
                    - '{{ Values[0] }}'
              DynamicParameters:
                - Key: '{{ Key }}'
                  Value:
                    Variable: '{{ Variable }}'
      - name: Integrations
        value:
          - PagerDutyConfiguration:
              Name: '{{ Name }}'
              SecretId: '{{ SecretId }}'
              PagerDutyIncidentConfiguration:
                ServiceId: '{{ ServiceId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: IncidentTemplate
        value:
          DedupeString: '{{ DedupeString }}'
          Impact: '{{ Impact }}'
          NotificationTargets:
            - SnsTopicArn: null
          Summary: '{{ Summary }}'
          Title: '{{ Title }}'
          IncidentTags:
            - null

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.ssmincidents.response_plans
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>response_plans</code> resource, the following permissions are required:

### Create
```json
ssm-incidents:CreateResponsePlan,
ssm-incidents:GetResponsePlan,
ssm-incidents:TagResource,
ssm-incidents:ListTagsForResource,
iam:PassRole,
secretsmanager:GetSecretValue,
kms:Decrypt,
kms:GenerateDataKey*
```

### Delete
```json
ssm-incidents:DeleteResponsePlan,
ssm-incidents:GetResponsePlan
```

### List
```json
ssm-incidents:ListResponsePlans
```

