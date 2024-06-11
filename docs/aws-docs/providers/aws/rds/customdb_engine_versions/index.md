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

Creates, updates, deletes or gets a <code>customdb_engine_version</code> resource or lists <code>customdb_engine_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customdb_engine_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.customdb_engine_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="database_installation_files_s3_bucket_name" /></td><td><code>string</code></td><td>The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.</td></tr>
<tr><td><CopyableCode code="database_installation_files_s3_prefix" /></td><td><code>string</code></td><td>The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012/cev1`. If this setting isn't specified, no prefix is assumed.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description of your CEV.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.</td></tr>
<tr><td><CopyableCode code="manifest" /></td><td><code>string</code></td><td>The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.</td></tr>
<tr><td><CopyableCode code="db_engine_version_arn" /></td><td><code>string</code></td><td>The ARN of the custom engine version.</td></tr>
<tr><td><CopyableCode code="source_custom_db_engine_version_identifier" /></td><td><code>string</code></td><td>The identifier of the source custom engine version.</td></tr>
<tr><td><CopyableCode code="use_aws_provided_latest_image" /></td><td><code>boolean</code></td><td>A value that indicates whether AWS provided latest image is applied automatically to the Custom Engine Version. By default, AWS provided latest image is applied automatically. This value is only applied on create.</td></tr>
<tr><td><CopyableCode code="image_id" /></td><td><code>string</code></td><td>The identifier of Amazon Machine Image (AMI) used for CEV.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The availability status to be assigned to the CEV.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="Engine, EngineVersion, region" /></td>
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
List all <code>customdb_engine_versions</code> in a region.
```sql
SELECT
region,
engine,
engine_version
FROM aws.rds.customdb_engine_versions
WHERE region = 'us-east-1';
```
Gets all properties from a <code>customdb_engine_version</code>.
```sql
SELECT
region,
database_installation_files_s3_bucket_name,
database_installation_files_s3_prefix,
description,
engine,
engine_version,
kms_key_id,
manifest,
db_engine_version_arn,
source_custom_db_engine_version_identifier,
use_aws_provided_latest_image,
image_id,
status,
tags
FROM aws.rds.customdb_engine_versions
WHERE region = 'us-east-1' AND data__Identifier = '<Engine>|<EngineVersion>';
```


## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
rds:DescribeDBEngineVersions
```

### Update
```json
rds:AddTagsToResource,
rds:DescribeDBEngineVersions,
rds:ModifyCustomDBEngineVersion,
rds:RemoveTagsFromResource
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

