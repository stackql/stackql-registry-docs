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
<tr><td><b>Description</b></td><td>Creates a custom DB engine version (CEV).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.customdb_engine_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="database_installation_files_s3_bucket_name" /></td><td><code>string</code></td><td>The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is <code>my-custom-installation-files</code>.</td></tr>
<tr><td><CopyableCode code="database_installation_files_s3_prefix" /></td><td><code>string</code></td><td>The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is <code>123456789012/cev1</code>. If this setting isn't specified, no prefix is assumed.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description of your CEV.</td></tr>
<tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The database engine to use for your custom engine version (CEV).<br />Valid values:<br />+ <code>custom-oracle-ee</code> <br />+ <code>custom-oracle-ee-cdb</code></td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The name of your CEV. The name format is <code>major version.customized_string</code>. For example, a valid CEV name is <code>19.my_cev1</code>. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of <code>Engine</code> and <code>EngineVersion</code> is unique per customer per Region.<br />*Constraints:* Minimum length is 1. Maximum length is 60.<br />*Pattern:* <code>^&#91;a-z0-9_.-&#93;&#123;1,60$</code>&#125;</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>The AWS KMS key identifier for an encrypted CEV. A symmetric encryption KMS key is required for RDS Custom, but optional for Amazon RDS.<br />If you have an existing symmetric encryption KMS key in your account, you can use it with RDS Custom. No further action is necessary. If you don't already have a symmetric encryption KMS key in your account, follow the instructions in &#91;Creating a symmetric encryption KMS key&#93;(https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html#create-symmetric-cmk) in the *Key Management Service Developer Guide*.<br />You can choose the same symmetric encryption key when you create a CEV and a DB instance, or choose different keys.</td></tr>
<tr><td><CopyableCode code="manifest" /></td><td><code>string</code></td><td>The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name/value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.<br />The following JSON fields are valid:<br />+ MediaImportTemplateVersion Version of the CEV manifest. The date is in the format YYYY-MM-DD. + databaseInstallationFileNames Ordered list of installation files for the CEV. + opatchFileNames Ordered list of OPatch installers used for the Oracle DB engine. + psuRuPatchFileNames The PSU and RU patches for this CEV. + OtherPatchFileNames The patches that are not in the list of PSU and RU patches. Amazon RDS applies these patches after applying the PSU and RU patches. <br />For more information, see &#91;Creating the CEV manifest&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-cev.html#custom-cev.preparing.manifest) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><CopyableCode code="db_engine_version_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_custom_db_engine_version_identifier" /></td><td><code>string</code></td><td>The ARN of a CEV to use as a source for creating a new CEV. You can specify a different Amazon Machine Imagine (AMI) by using either <code>Source</code> or <code>UseAwsProvidedLatestImage</code>. You can't specify a different JSON manifest when you specify <code>SourceCustomDbEngineVersionIdentifier</code>.</td></tr>
<tr><td><CopyableCode code="use_aws_provided_latest_image" /></td><td><code>boolean</code></td><td>Specifies whether to use the latest service-provided Amazon Machine Image (AMI) for the CEV. If you specify <code>UseAwsProvidedLatestImage</code>, you can't also specify <code>ImageId</code>.</td></tr>
<tr><td><CopyableCode code="image_id" /></td><td><code>string</code></td><td>A value that indicates the ID of the AMI.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>A value that indicates the status of a custom engine version (CEV).</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of tags. For more information, see &#91;Tagging Amazon RDS Resources&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide.*</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-customdbengineversion.html"><code>AWS::RDS::CustomDBEngineVersion</code></a>.

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
Gets all <code>customdb_engine_versions</code> in a region.
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
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>customdb_engine_version</code>.
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
