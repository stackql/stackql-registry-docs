---
title: location_s3s
hide_title: false
hide_table_of_contents: false
keywords:
  - location_s3s
  - datasync
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


Used to retrieve a list of <code>location_s3s</code> in a region or to create or delete a <code>location_s3s</code> resource, use <code>location_s3</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_s3s</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationS3</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_s3s" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon S3 bucket location.</td></tr>
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
location_arn
FROM aws.datasync.location_s3s
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
 "S3Config": {
  "BucketAccessRoleArn": "{{ BucketAccessRoleArn }}"
 }
}
>>>
--required properties only
INSERT INTO aws.datasync.location_s3s (
 S3Config,
 region
)
SELECT 
{{ S3Config }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "S3Config": {
  "BucketAccessRoleArn": "{{ BucketAccessRoleArn }}"
 },
 "S3BucketArn": "{{ S3BucketArn }}",
 "Subdirectory": "{{ Subdirectory }}",
 "S3StorageClass": "{{ S3StorageClass }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.datasync.location_s3s (
 S3Config,
 S3BucketArn,
 Subdirectory,
 S3StorageClass,
 Tags,
 region
)
SELECT 
 {{ S3Config }},
 {{ S3BucketArn }},
 {{ Subdirectory }},
 {{ S3StorageClass }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.datasync.location_s3s
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>location_s3s</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationS3,
datasync:DescribeLocationS3,
datasync:ListTagsForResource,
datasync:TagResource,
s3:ListAllMyBuckets,
s3:ListBucket,
iam:GetRole,
iam:PassRole
```

### Delete
```json
datasync:DeleteLocation
```

### List
```json
datasync:ListLocations
```

