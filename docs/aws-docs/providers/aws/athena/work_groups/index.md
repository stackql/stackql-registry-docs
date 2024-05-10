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


Used to retrieve a list of <code>work_groups</code> in a region or to create or delete a <code>work_groups</code> resource, use <code>work_group</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>work_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Athena::WorkGroup</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.athena.work_groups" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The workGroup name.</td></tr>
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
name
FROM aws.athena.work_groups
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>work_group</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- work_group.iql (required properties only)
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
-- work_group.iql (all properties)
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

## `DELETE` Example

```sql
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

