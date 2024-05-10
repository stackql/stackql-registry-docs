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


Used to retrieve a list of <code>assessments</code> in a region or to create or delete a <code>assessments</code> resource, use <code>assessment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An entity that defines the scope of audit evidence collected by AWS Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.auditmanager.assessments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="assessment_id" /></td><td><code>undefined</code></td><td></td></tr>
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
assessment_id
FROM aws.auditmanager.assessments
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>assessment</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- assessment.iql (required properties only)
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
-- assessment.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
auditmanager:DeleteAssessment
```

### List
```json
auditmanager:ListAssessments
```

