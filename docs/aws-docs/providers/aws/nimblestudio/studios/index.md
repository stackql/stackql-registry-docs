---
title: studios
hide_title: false
hide_table_of_contents: false
keywords:
  - studios
  - nimblestudio
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

Creates, updates, deletes or gets a <code>studio</code> resource or lists <code>studios</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a studio that contains other Nimble Studio resources</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.studios" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="admin_role_arn" /></td><td><code>string</code></td><td><p>The IAM role that Studio Admins will assume when logging in to the Nimble Studio portal.</p></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td><p>A friendly name for the studio.</p></td></tr>
<tr><td><CopyableCode code="home_region" /></td><td><code>string</code></td><td><p>The Amazon Web Services Region where the studio resource is located.</p></td></tr>
<tr><td><CopyableCode code="sso_client_id" /></td><td><code>string</code></td><td><p>The Amazon Web Services SSO application client ID used to integrate with Amazon Web Services SSO to enable Amazon Web Services SSO users to log in to Nimble Studio portal.</p></td></tr>
<tr><td><CopyableCode code="studio_encryption_configuration" /></td><td><code>object</code></td><td><p>Configuration of the encryption method that is used for the studio.</p></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_name" /></td><td><code>string</code></td><td><p>The studio name that is used in the URL of the Nimble Studio portal when accessed by Nimble Studio users.</p></td></tr>
<tr><td><CopyableCode code="studio_url" /></td><td><code>string</code></td><td><p>The address of the web page for the studio.</p></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="user_role_arn" /></td><td><code>string</code></td><td><p>The IAM role that Studio Users will assume when logging in to the Nimble Studio portal.</p></td></tr>
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
    <td><CopyableCode code="DisplayName, UserRoleArn, AdminRoleArn, StudioName, region" /></td>
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
Gets all <code>studios</code> in a region.
```sql
SELECT
region,
admin_role_arn,
display_name,
home_region,
sso_client_id,
studio_encryption_configuration,
studio_id,
studio_name,
studio_url,
tags,
user_role_arn
FROM aws.nimblestudio.studios
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>studio</code>.
```sql
SELECT
region,
admin_role_arn,
display_name,
home_region,
sso_client_id,
studio_encryption_configuration,
studio_id,
studio_name,
studio_url,
tags,
user_role_arn
FROM aws.nimblestudio.studios
WHERE region = 'us-east-1' AND data__Identifier = '<StudioId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>studio</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.nimblestudio.studios (
 AdminRoleArn,
 DisplayName,
 StudioName,
 UserRoleArn,
 region
)
SELECT 
'{{ AdminRoleArn }}',
 '{{ DisplayName }}',
 '{{ StudioName }}',
 '{{ UserRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.nimblestudio.studios (
 AdminRoleArn,
 DisplayName,
 StudioEncryptionConfiguration,
 StudioName,
 Tags,
 UserRoleArn,
 region
)
SELECT 
 '{{ AdminRoleArn }}',
 '{{ DisplayName }}',
 '{{ StudioEncryptionConfiguration }}',
 '{{ StudioName }}',
 '{{ Tags }}',
 '{{ UserRoleArn }}',
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
  - name: studio
    props:
      - name: AdminRoleArn
        value: '{{ AdminRoleArn }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: StudioEncryptionConfiguration
        value:
          KeyType: '{{ KeyType }}'
          KeyArn: '{{ KeyArn }}'
      - name: StudioName
        value: '{{ StudioName }}'
      - name: Tags
        value: {}
      - name: UserRoleArn
        value: '{{ UserRoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.nimblestudio.studios
WHERE data__Identifier = '<StudioId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>studios</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
nimble:CreateStudio,
nimble:GetStudio,
nimble:TagResource,
sso:CreateManagedApplicationInstance,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey
```

### Read
```json
nimble:GetStudio,
kms:Encrypt,
kms:Decrypt,
kms:ListGrants,
kms:GenerateDataKey
```

### Update
```json
iam:PassRole,
nimble:UpdateStudio,
nimble:GetStudio,
kms:Encrypt,
kms:Decrypt,
kms:CreateGrant,
kms:ListGrants,
kms:GenerateDataKey
```

### Delete
```json
nimble:DeleteStudio,
nimble:GetStudio,
nimble:UntagResource,
kms:Encrypt,
kms:Decrypt,
kms:ListGrants,
kms:RetireGrant,
kms:GenerateDataKey,
sso:DeleteManagedApplicationInstance,
sso:GetManagedApplicationInstance
```

### List
```json
nimble:ListStudios
```

