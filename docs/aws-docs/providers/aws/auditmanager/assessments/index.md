---
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
  - auditmanager
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

Creates, updates, deletes or gets an <code>assessment</code> resource or lists <code>assessments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An entity that defines the scope of audit evidence collected by AWS Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.auditmanager.assessments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="framework_id" /></td><td><code>string</code></td><td>The identifier for the specified framework.</td></tr>
<tr><td><CopyableCode code="assessment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account" /></td><td><code>object</code></td><td>The AWS account associated with the assessment.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the assessment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags associated with the assessment.</td></tr>
<tr><td><CopyableCode code="delegations" /></td><td><code>array</code></td><td>The list of delegations.</td></tr>
<tr><td><CopyableCode code="roles" /></td><td><code>array</code></td><td>The list of roles for the specified assessment.</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>object</code></td><td>The wrapper that contains the AWS accounts and AWS services in scope for the assessment.</td></tr>
<tr><td><CopyableCode code="assessment_reports_destination" /></td><td><code>object</code></td><td>The destination in which evidence reports are stored for the specified assessment.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the specified assessment.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>number</code></td><td>The sequence of characters that identifies when the event occurred.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the related assessment.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the specified assessment.</td></tr>
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
List all <code>assessments</code> in a region.
```sql
SELECT
region,
assessment_id
FROM aws.auditmanager.assessments
WHERE region = 'us-east-1';
```
Gets all properties from an <code>assessment</code>.
```sql
SELECT
region,
framework_id,
assessment_id,
aws_account,
arn,
tags,
delegations,
roles,
scope,
assessment_reports_destination,
status,
creation_time,
name,
description
FROM aws.auditmanager.assessments
WHERE region = 'us-east-1' AND data__Identifier = '<AssessmentId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assessment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.auditmanager.assessments (
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
INSERT INTO aws.auditmanager.assessments (
 FrameworkId,
 AwsAccount,
 Tags,
 Delegations,
 Roles,
 Scope,
 AssessmentReportsDestination,
 Status,
 Name,
 Description,
 region
)
SELECT 
 '{{ FrameworkId }}',
 '{{ AwsAccount }}',
 '{{ Tags }}',
 '{{ Delegations }}',
 '{{ Roles }}',
 '{{ Scope }}',
 '{{ AssessmentReportsDestination }}',
 '{{ Status }}',
 '{{ Name }}',
 '{{ Description }}',
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
  - name: assessment
    props:
      - name: FrameworkId
        value: '{{ FrameworkId }}'
      - name: AwsAccount
        value:
          Id: '{{ Id }}'
          EmailAddress: '{{ EmailAddress }}'
          Name: '{{ Name }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Delegations
        value:
          - LastUpdated: null
            ControlSetId: '{{ ControlSetId }}'
            CreationTime: null
            CreatedBy: '{{ CreatedBy }}'
            RoleArn: '{{ RoleArn }}'
            AssessmentName: '{{ AssessmentName }}'
            Comment: '{{ Comment }}'
            Id: '{{ Id }}'
            RoleType: '{{ RoleType }}'
            AssessmentId: null
            Status: '{{ Status }}'
      - name: Roles
        value:
          - RoleArn: null
            RoleType: null
      - name: Scope
        value:
          AwsAccounts:
            - null
          AwsServices:
            - ServiceName: '{{ ServiceName }}'
      - name: AssessmentReportsDestination
        value:
          Destination: '{{ Destination }}'
          DestinationType: '{{ DestinationType }}'
      - name: Status
        value: '{{ Status }}'
      - name: Name
        value: null
      - name: Description
        value: '{{ Description }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.auditmanager.assessments
WHERE data__Identifier = '<AssessmentId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>assessments</code> resource, the following permissions are required:

### Create
```json
auditmanager:CreateAssessment,
auditmanager:TagResource,
auditmanager:ListTagsForResource,
auditmanager:BatchCreateDelegationByAssessment,
iam:PassRole
```

### Read
```json
auditmanager:GetAssessment
```

### Update
```json
auditmanager:UpdateAssessment,
auditmanager:UpdateAssessmentStatus,
auditmanager:BatchCreateDelegationByAssessment,
auditmanager:BatchDeleteDelegationByAssessment
```

### Delete
```json
auditmanager:DeleteAssessment
```

### List
```json
auditmanager:ListAssessments
```

