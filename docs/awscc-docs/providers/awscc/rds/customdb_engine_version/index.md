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
<tr><td><b>Description</b></td><td>customdb_engine_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.rds.customdb_engine_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>database_installation_files_s3_bucket_name</code></td><td><code>string</code></td><td>The name of an Amazon S3 bucket that contains database installation files for your CEV. For example, a valid bucket name is `my-custom-installation-files`.</td></tr>
<tr><td><code>database_installation_files_s3_prefix</code></td><td><code>string</code></td><td>The Amazon S3 directory that contains the database installation files for your CEV. For example, a valid bucket name is `123456789012&#x2F;cev1`. If this setting isn't specified, no prefix is assumed.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>An optional description of your CEV.</td></tr>
<tr><td><code>engine</code></td><td><code>string</code></td><td>The database engine to use for your custom engine version (CEV). The only supported value is `custom-oracle-ee`.</td></tr>
<tr><td><code>engine_version</code></td><td><code>string</code></td><td>The name of your CEV. The name format is 19.customized_string . For example, a valid name is 19.my_cev1. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of Engine and EngineVersion is unique per customer per Region.</td></tr>
<tr><td><code>k_ms_key_id</code></td><td><code>string</code></td><td>The AWS KMS key identifier for an encrypted CEV. A symmetric KMS key is required for RDS Custom, but optional for Amazon RDS.</td></tr>
<tr><td><code>manifest</code></td><td><code>string</code></td><td>The CEV manifest, which is a JSON document that describes the installation .zip files stored in Amazon S3. Specify the name&#x2F;value pairs in a file or a quoted string. RDS Custom applies the patches in the order in which they are listed.</td></tr>
<tr><td><code>d_bengine_version_arn</code></td><td><code>string</code></td><td>The ARN of the custom engine version.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The availability status to be assigned to the CEV.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
database_installation_files_s3_bucket_name,
database_installation_files_s3_prefix,
description,
engine,
engine_version,
k_ms_key_id,
manifest,
d_bengine_version_arn,
status,
tags
FROM awscc.rds.customdb_engine_version
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Engine&gt;'
AND data__Identifier = '&lt;EngineVersion&gt;'
```
