---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - qbusiness
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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::Application Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="attachments_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_center_application_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_center_instance_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="DisplayName, region" /></td>
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
Gets all <code>applications</code> in a region.
```sql
SELECT
region,
application_arn,
application_id,
attachments_configuration,
created_at,
description,
display_name,
encryption_configuration,
identity_center_application_arn,
identity_center_instance_arn,
role_arn,
status,
tags,
updated_at
FROM aws.qbusiness.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
application_arn,
application_id,
attachments_configuration,
created_at,
description,
display_name,
encryption_configuration,
identity_center_application_arn,
identity_center_instance_arn,
role_arn,
status,
tags,
updated_at
FROM aws.qbusiness.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.applications (
 DisplayName,
 region
)
SELECT 
'{{ DisplayName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.applications (
 AttachmentsConfiguration,
 Description,
 DisplayName,
 EncryptionConfiguration,
 IdentityCenterInstanceArn,
 RoleArn,
 Tags,
 region
)
SELECT 
 '{{ AttachmentsConfiguration }}',
 '{{ Description }}',
 '{{ DisplayName }}',
 '{{ EncryptionConfiguration }}',
 '{{ IdentityCenterInstanceArn }}',
 '{{ RoleArn }}',
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
  - name: application
    props:
      - name: AttachmentsConfiguration
        value:
          AttachmentsControlMode: '{{ AttachmentsControlMode }}'
      - name: Description
        value: '{{ Description }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: EncryptionConfiguration
        value:
          KmsKeyId: '{{ KmsKeyId }}'
      - name: IdentityCenterInstanceArn
        value: '{{ IdentityCenterInstanceArn }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
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
DELETE FROM aws.qbusiness.applications
WHERE data__Identifier = '<ApplicationId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
kms:CreateGrant,
kms:DescribeKey,
qbusiness:CreateApplication,
qbusiness:GetApplication,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
sso:CreateApplication,
sso:DeleteApplication,
sso:PutApplicationAccessScope,
sso:PutApplicationAuthenticationMethod,
sso:PutApplicationGrant
```

### Read
```json
qbusiness:GetApplication,
qbusiness:ListTagsForResource
```

### Update
```json
iam:PassRole,
qbusiness:GetApplication,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UntagResource,
qbusiness:UpdateApplication,
sso:CreateApplication,
sso:DeleteApplication,
sso:PutApplicationAccessScope,
sso:PutApplicationAuthenticationMethod,
sso:PutApplicationGrant
```

### Delete
```json
kms:RetireGrant,
qbusiness:DeleteApplication,
qbusiness:GetApplication,
sso:DeleteApplication
```

### List
```json
qbusiness:ListApplications
```

