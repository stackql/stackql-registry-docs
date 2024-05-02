---
title: customdb_engine_version
hide_title: false
hide_table_of_contents: false
keywords:
  - customdb_engine_version
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
Gets an individual <code>customdb_engine_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customdb_engine_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::RDS::CustomDBEngineVersion resource creates an Amazon RDS custom DB engine version.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.rds.customdb_engine_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>database_installation_files_s3_bucket_name</code></td><td><code>string</code></td><td>The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.</td></tr>
<tr><td><code>database_installation_files_s3_prefix</code></td><td><code>string</code></td><td>The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012&#x2F;cev1`. If this setting isn't specified, no prefix is assumed.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>An optional description of your CEV.</td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td>The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.</td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td>The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.</td></tr>
<tr><td><code>manifest</code></td><td><code>string</code></td><td>The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name&#x2F;value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.</td></tr>
<tr><td><code>db_engine_version_arn</code></td><td><code>string</code></td><td>The ARN of the custom engine version.</td></tr>
<tr><td><code>source_custom_db_engine_version_identifier</code></td><td><code>string</code></td><td>The identifier of the source custom engine version.</td></tr>
<tr><td><code>use_aws_provided_latest_image</code></td><td><code>boolean</code></td><td>A value that indicates whether AWS provided latest image is applied automatically to the Custom Engine Version. By default, AWS provided latest image is applied automatically. This value is only applied on create.</td></tr>
<tr><td><code>image_id</code></td><td><code>string</code></td><td>The identifier of Amazon Machine Image (AMI) used for CEV.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The availability status to be assigned to the CEV.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.rds.customdb_engine_version
WHERE data__Identifier = '<Engine>|<EngineVersion>';
```

## Permissions

To operate on the <code>customdb_engine_version</code> resource, the following permissions are required:

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

