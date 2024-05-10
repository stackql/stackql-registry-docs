---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - s3outposts
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


Used to retrieve a list of <code>buckets</code> in a region or to create or delete a <code>buckets</code> resource, use <code>bucket</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::Bucket</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3outposts.buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified bucket.</td></tr>
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
arn
FROM aws.s3outposts.buckets
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
 "BucketName": "{{ BucketName }}",
 "OutpostId": "{{ OutpostId }}"
}
>>>
--required properties only
INSERT INTO aws.s3outposts.buckets (
 BucketName,
 OutpostId,
 region
)
SELECT 
{{ BucketName }},
 {{ OutpostId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "BucketName": "{{ BucketName }}",
 "OutpostId": "{{ OutpostId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "LifecycleConfiguration": {
  "Rules": [
   {
    "Status": "{{ Status }}",
    "Id": "{{ Id }}",
    "AbortIncompleteMultipartUpload": {
     "DaysAfterInitiation": "{{ DaysAfterInitiation }}"
    },
    "ExpirationDate": "{{ ExpirationDate }}",
    "ExpirationInDays": "{{ ExpirationInDays }}",
    "Filter": {
     "Prefix": "{{ Prefix }}",
     "Tag": {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}"
     },
     "AndOperator": null
    }
   }
  ]
 }
}
>>>
--all properties
INSERT INTO aws.s3outposts.buckets (
 BucketName,
 OutpostId,
 Tags,
 LifecycleConfiguration,
 region
)
SELECT 
 {{ BucketName }},
 {{ OutpostId }},
 {{ Tags }},
 {{ LifecycleConfiguration }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.s3outposts.buckets
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>buckets</code> resource, the following permissions are required:

### Create
```json
s3-outposts:CreateBucket,
s3-outposts:PutBucketTagging,
s3-outposts:PutLifecycleConfiguration
```

### Delete
```json
s3-outposts:DeleteBucket
```

### List
```json
s3-outposts:ListRegionalBuckets
```

