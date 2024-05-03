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

Used to retrieve a list of <code>customdb_engine_versions</code> in a region or create a <code>customdb_engine_versions</code> resource, use <code>customdb_engine_version</code> to operate on an individual resource.

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
WHERE region = 'us-east-1'
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

### List
```json
rds:DescribeDBEngineVersions
```
