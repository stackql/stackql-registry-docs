---
title: directory_buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - directory_buckets
  - s3express
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


Used to retrieve a list of <code>directory_buckets</code> in a region or to create or delete a <code>directory_buckets</code> resource, use <code>directory_bucket</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::S3Express::DirectoryBucket.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3express.directory_buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>Specifies a name for the bucket. The bucket name must contain only lowercase letters, numbers, and hyphens (-). A directory bucket name must be unique in the chosen Availability Zone. The bucket name must also follow the format 'bucket_base_name--az_id--x-s3' (for example, 'DOC-EXAMPLE-BUCKET--usw2-az1--x-s3'). If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the bucket name.</td></tr>
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
bucket_name
FROM aws.s3express.directory_buckets
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "LocationName": "{{ LocationName }}",
 "DataRedundancy": "{{ DataRedundancy }}"
}
>>>
--required properties only
INSERT INTO aws.s3express.directory_buckets (
 LocationName,
 DataRedundancy,
 region
)
SELECT 
{{ .LocationName }},
 {{ .DataRedundancy }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "BucketName": "{{ BucketName }}",
 "LocationName": "{{ LocationName }}",
 "DataRedundancy": "{{ DataRedundancy }}"
}
>>>
--all properties
INSERT INTO aws.s3express.directory_buckets (
 BucketName,
 LocationName,
 DataRedundancy,
 region
)
SELECT 
 {{ .BucketName }},
 {{ .LocationName }},
 {{ .DataRedundancy }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3express.directory_buckets
WHERE data__Identifier = '<BucketName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>directory_buckets</code> resource, the following permissions are required:

### Create
```json
s3express:CreateBucket,
s3express:ListAllMyDirectoryBuckets
```

### Delete
```json
s3express:DeleteBucket,
s3express:ListAllMyDirectoryBuckets
```

### List
```json
s3express:ListAllMyDirectoryBuckets
```

