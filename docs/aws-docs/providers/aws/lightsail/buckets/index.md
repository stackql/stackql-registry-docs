---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - lightsail
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
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Bucket</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>The name for the bucket.</td></tr>
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
FROM aws.lightsail.buckets
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
 "BundleId": "{{ BundleId }}"
}
>>>
--required properties only
INSERT INTO aws.lightsail.buckets (
 BucketName,
 BundleId,
 region
)
SELECT 
{{ BucketName }},
 {{ BundleId }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "BucketName": "{{ BucketName }}",
 "BundleId": "{{ BundleId }}",
 "ObjectVersioning": "{{ ObjectVersioning }}",
 "AccessRules": {
  "GetObject": "{{ GetObject }}",
  "AllowPublicOverrides": "{{ AllowPublicOverrides }}"
 },
 "ResourcesReceivingAccess": [
  "{{ ResourcesReceivingAccess[0] }}"
 ],
 "ReadOnlyAccessAccounts": [
  "{{ ReadOnlyAccessAccounts[0] }}"
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.lightsail.buckets (
 BucketName,
 BundleId,
 ObjectVersioning,
 AccessRules,
 ResourcesReceivingAccess,
 ReadOnlyAccessAccounts,
 Tags,
 region
)
SELECT 
 {{ BucketName }},
 {{ BundleId }},
 {{ ObjectVersioning }},
 {{ AccessRules }},
 {{ ResourcesReceivingAccess }},
 {{ ReadOnlyAccessAccounts }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.lightsail.buckets
WHERE data__Identifier = '<BucketName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>buckets</code> resource, the following permissions are required:

### Create
```json
lightsail:CreateBucket,
lightsail:GetBuckets,
lightsail:GetInstance,
lightsail:UpdateBucket,
lightsail:UpdateBucketBundle,
lightsail:SetResourceAccessForBucket,
lightsail:TagResource,
lightsail:UntagResource
```

### Delete
```json
lightsail:DeleteBucket,
lightsail:GetBuckets
```

### List
```json
lightsail:GetBuckets
```

