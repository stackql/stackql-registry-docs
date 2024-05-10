---
title: customdb_engine_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - customdb_engine_versions
  - rds
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


Used to retrieve a list of <code>customdb_engine_versions</code> in a region or to create or delete a <code>customdb_engine_versions</code> resource, use <code>customdb_engine_version</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customdb_engine_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.customdb_engine_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.</td></tr>
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
engine,
engine_version
FROM aws.rds.customdb_engine_versions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>customdb_engine_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- customdb_engine_version.iql (required properties only)
INSERT INTO aws.rds.customdb_engine_versions (
 Engine,
 EngineVersion,
 region
)
SELECT 
'{{ Engine }}',
 '{{ EngineVersion }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- customdb_engine_version.iql (all properties)
INSERT INTO aws.rds.customdb_engine_versions (
 DatabaseInstallationFilesS3BucketName,
 DatabaseInstallationFilesS3Prefix,
 Description,
 Engine,
 EngineVersion,
 KMSKeyId,
 Manifest,
 SourceCustomDbEngineVersionIdentifier,
 UseAwsProvidedLatestImage,
 ImageId,
 Status,
 Tags,
 region
)
SELECT 
 '{{ DatabaseInstallationFilesS3BucketName }}',
 '{{ DatabaseInstallationFilesS3Prefix }}',
 '{{ Description }}',
 '{{ Engine }}',
 '{{ EngineVersion }}',
 '{{ KMSKeyId }}',
 '{{ Manifest }}',
 '{{ SourceCustomDbEngineVersionIdentifier }}',
 '{{ UseAwsProvidedLatestImage }}',
 '{{ ImageId }}',
 '{{ Status }}',
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
  - name: customdb_engine_version
    props:
      - name: DatabaseInstallationFilesS3BucketName
        value: '{{ DatabaseInstallationFilesS3BucketName }}'
      - name: DatabaseInstallationFilesS3Prefix
        value: '{{ DatabaseInstallationFilesS3Prefix }}'
      - name: Description
        value: '{{ Description }}'
      - name: Engine
        value: '{{ Engine }}'
      - name: EngineVersion
        value: '{{ EngineVersion }}'
      - name: KMSKeyId
        value: '{{ KMSKeyId }}'
      - name: Manifest
        value: '{{ Manifest }}'
      - name: SourceCustomDbEngineVersionIdentifier
        value: '{{ SourceCustomDbEngineVersionIdentifier }}'
      - name: UseAwsProvidedLatestImage
        value: '{{ UseAwsProvidedLatestImage }}'
      - name: ImageId
        value: '{{ ImageId }}'
      - name: Status
        value: '{{ Status }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.customdb_engine_versions
WHERE data__Identifier = '<Engine|EngineVersion>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>customdb_engine_versions</code> resource, the following permissions are required:

### Create
```json
ec2:CopySnapshot,
ec2:DeleteSnapshot,
ec2:DescribeSnapshots,
kms:CreateGrant,
kms:Decrypt,
kms:DescribeKey,
kms:GenerateDataKey,
kms:ReEncrypt,
mediaimport:CreateDatabaseBinarySnapshot,
rds:AddTagsToResource,
rds:CreateCustomDBEngineVersion,
rds:DescribeDBEngineVersions,
rds:ModifyCustomDBEngineVersion,
s3:CreateBucket,
s3:GetObject,
s3:GetObjectAcl,
s3:GetObjectTagging,
s3:ListBucket,
s3:PutBucketObjectLockConfiguration,
s3:PutBucketPolicy,
s3:PutBucketVersioning
```

### Delete
```json
rds:DeleteCustomDBEngineVersion,
rds:DescribeDBEngineVersions
```

### List
```json
rds:DescribeDBEngineVersions
```

