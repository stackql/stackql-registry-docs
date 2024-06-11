---
title: work_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - work_groups
  - athena
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

Creates, updates, deletes or gets a <code>work_group</code> resource or lists <code>work_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::WorkGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.work_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The workGroup name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The workgroup description.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags, separated by commas, that you want to attach to the workgroup as you create it</td></tr>
<tr><td><CopyableCode code="work_group_configuration" /></td><td><code>object</code></td><td>The workgroup configuration</td></tr>
<tr><td><CopyableCode code="work_group_configuration_updates" /></td><td><code>object</code></td><td>The workgroup configuration update object</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The date and time the workgroup was created.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the workgroup: ENABLED or DISABLED.</td></tr>
<tr><td><CopyableCode code="recursive_delete_option" /></td><td><code>boolean</code></td><td>The option to delete the workgroup and its contents even if the workgroup contains any named queries.</td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
List all <code>work_groups</code> in a region.
```sql
SELECT
region,
name
FROM aws.athena.work_groups
WHERE region = 'us-east-1';
```
Gets all properties from a <code>work_group</code>.
```sql
SELECT
region,
name,
description,
tags,
work_group_configuration,
work_group_configuration_updates,
creation_time,
state,
recursive_delete_option
FROM aws.athena.work_groups
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>work_group</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.athena.work_groups (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.athena.work_groups (
 Name,
 Description,
 Tags,
 WorkGroupConfiguration,
 WorkGroupConfigurationUpdates,
 State,
 RecursiveDeleteOption,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Tags }}',
 '{{ WorkGroupConfiguration }}',
 '{{ WorkGroupConfigurationUpdates }}',
 '{{ State }}',
 '{{ RecursiveDeleteOption }}',
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
  - name: work_group
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: WorkGroupConfiguration
        value:
          BytesScannedCutoffPerQuery: '{{ BytesScannedCutoffPerQuery }}'
          EnforceWorkGroupConfiguration: '{{ EnforceWorkGroupConfiguration }}'
          PublishCloudWatchMetricsEnabled: '{{ PublishCloudWatchMetricsEnabled }}'
          RequesterPaysEnabled: '{{ RequesterPaysEnabled }}'
          ResultConfiguration:
            EncryptionConfiguration:
              EncryptionOption: '{{ EncryptionOption }}'
              KmsKey: '{{ KmsKey }}'
            OutputLocation: '{{ OutputLocation }}'
            ExpectedBucketOwner: '{{ ExpectedBucketOwner }}'
            AclConfiguration:
              S3AclOption: '{{ S3AclOption }}'
          EngineVersion:
            SelectedEngineVersion: '{{ SelectedEngineVersion }}'
            EffectiveEngineVersion: '{{ EffectiveEngineVersion }}'
          AdditionalConfiguration: '{{ AdditionalConfiguration }}'
          ExecutionRole: '{{ ExecutionRole }}'
          CustomerContentEncryptionConfiguration:
            KmsKey: null
      - name: WorkGroupConfigurationUpdates
        value:
          BytesScannedCutoffPerQuery: null
          EnforceWorkGroupConfiguration: null
          PublishCloudWatchMetricsEnabled: null
          RequesterPaysEnabled: null
          ResultConfigurationUpdates:
            EncryptionConfiguration: null
            OutputLocation: null
            ExpectedBucketOwner: null
            AclConfiguration: null
            RemoveEncryptionConfiguration: '{{ RemoveEncryptionConfiguration }}'
            RemoveOutputLocation: '{{ RemoveOutputLocation }}'
            RemoveExpectedBucketOwner: '{{ RemoveExpectedBucketOwner }}'
            RemoveAclConfiguration: '{{ RemoveAclConfiguration }}'
          RemoveBytesScannedCutoffPerQuery: '{{ RemoveBytesScannedCutoffPerQuery }}'
          EngineVersion: null
          AdditionalConfiguration: null
          ExecutionRole: null
          CustomerContentEncryptionConfiguration: null
          RemoveCustomerContentEncryptionConfiguration: '{{ RemoveCustomerContentEncryptionConfiguration }}'
      - name: State
        value: '{{ State }}'
      - name: RecursiveDeleteOption
        value: '{{ RecursiveDeleteOption }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.athena.work_groups
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>work_groups</code> resource, the following permissions are required:

### Create
```json
athena:CreateWorkGroup,
athena:TagResource,
iam:PassRole,
s3:GetBucketLocation,
s3:GetObject,
s3:ListBucket,
s3:ListBucketMultipartUploads,
s3:AbortMultipartUpload,
s3:PutObject,
s3:ListMultipartUploadParts,
kms:Decrypt,
kms:GenerateDataKey
```

### Read
```json
athena:GetWorkGroup,
athena:ListTagsForResource
```

### List
```json
athena:ListWorkGroups
```

### Delete
```json
athena:DeleteWorkGroup,
athena:GetWorkGroup,
athena:UntagResource
```

### Update
```json
athena:UpdateWorkGroup,
athena:TagResource,
athena:UntagResource,
iam:PassRole,
s3:GetBucketLocation,
s3:GetObject,
s3:ListBucket,
s3:ListBucketMultipartUploads,
s3:AbortMultipartUpload,
s3:PutObject,
s3:ListMultipartUploadParts,
kms:Decrypt,
kms:GenerateDataKey
```

