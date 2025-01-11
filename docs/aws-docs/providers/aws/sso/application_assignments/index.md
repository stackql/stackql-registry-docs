---
title: application_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - application_assignments
  - sso
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

Creates, updates, deletes or gets an <code>application_assignment</code> resource or lists <code>application_assignments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO application access grant to a user or group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.application_assignments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the application.</td></tr>
<tr><td><CopyableCode code="principal_type" /></td><td><code>string</code></td><td>The entity type for which the assignment will be created.</td></tr>
<tr><td><CopyableCode code="principal_id" /></td><td><code>string</code></td><td>An identifier for an object in IAM Identity Center, such as a user or group</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-applicationassignment.html"><code>AWS::SSO::ApplicationAssignment</code></a>.

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
    <td><CopyableCode code="ApplicationArn, PrincipalType, PrincipalId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>application_assignments</code> in a region.
```sql
SELECT
region,
application_arn,
principal_type,
principal_id
FROM aws.sso.application_assignments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application_assignment</code>.
```sql
SELECT
region,
application_arn,
principal_type,
principal_id
FROM aws.sso.application_assignments
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationArn>|<PrincipalType>|<PrincipalId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_assignment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.sso.application_assignments (
 ApplicationArn,
 PrincipalType,
 PrincipalId,
 region
)
SELECT 
'{{ ApplicationArn }}',
 '{{ PrincipalType }}',
 '{{ PrincipalId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.sso.application_assignments (
 ApplicationArn,
 PrincipalType,
 PrincipalId,
 region
)
SELECT 
 '{{ ApplicationArn }}',
 '{{ PrincipalType }}',
 '{{ PrincipalId }}',
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
  - name: application_assignment
    props:
      - name: ApplicationArn
        value: '{{ ApplicationArn }}'
      - name: PrincipalType
        value: '{{ PrincipalType }}'
      - name: PrincipalId
        value: '{{ PrincipalId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.sso.application_assignments
WHERE data__Identifier = '<ApplicationArn|PrincipalType|PrincipalId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>application_assignments</code> resource, the following permissions are required:

### Create
```json
sso:CreateApplicationAssignment,
sso:DescribeApplicationAssignment
```

### Read
```json
sso:DescribeApplicationAssignment
```

### Delete
```json
sso:DeleteApplicationAssignment
```

### List
```json
sso:ListApplicationAssignments
```
