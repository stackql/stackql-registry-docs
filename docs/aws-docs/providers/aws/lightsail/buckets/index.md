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

Creates, updates, deletes or gets a <code>bucket</code> resource or lists <code>buckets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Bucket</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.buckets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td>The name for the bucket.</td></tr>
<tr><td><CopyableCode code="bundle_id" /></td><td><code>string</code></td><td>The ID of the bundle to use for the bucket.</td></tr>
<tr><td><CopyableCode code="bucket_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="object_versioning" /></td><td><code>boolean</code></td><td>Specifies whether to enable or disable versioning of objects in the bucket.</td></tr>
<tr><td><CopyableCode code="access_rules" /></td><td><code>object</code></td><td>An object that sets the public accessibility of objects in the specified bucket.</td></tr>
<tr><td><CopyableCode code="resources_receiving_access" /></td><td><code>array</code></td><td>The names of the Lightsail resources for which to set bucket access.</td></tr>
<tr><td><CopyableCode code="read_only_access_accounts" /></td><td><code>array</code></td><td>An array of strings to specify the AWS account IDs that can access the bucket.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The URL of the bucket.</td></tr>
<tr><td><CopyableCode code="able_to_update_bundle" /></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to a bucket can be changed to another bundle. You can update a bucket's bundle only one time within a monthly AWS billing cycle.</td></tr>
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
    <td><CopyableCode code="BucketName, BundleId, region" /></td>
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
Gets all <code>buckets</code> in a region.
```sql
SELECT
region,
bucket_name,
bundle_id,
bucket_arn,
object_versioning,
access_rules,
resources_receiving_access,
read_only_access_accounts,
tags,
url,
able_to_update_bundle
FROM aws.lightsail.buckets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>bucket</code>.
```sql
SELECT
region,
bucket_name,
bundle_id,
bucket_arn,
object_versioning,
access_rules,
resources_receiving_access,
read_only_access_accounts,
tags,
url,
able_to_update_bundle
FROM aws.lightsail.buckets
WHERE region = 'us-east-1' AND data__Identifier = '<BucketName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bucket</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lightsail.buckets (
 BucketName,
 BundleId,
 region
)
SELECT 
'{{ BucketName }}',
 '{{ BundleId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ BucketName }}',
 '{{ BundleId }}',
 '{{ ObjectVersioning }}',
 '{{ AccessRules }}',
 '{{ ResourcesReceivingAccess }}',
 '{{ ReadOnlyAccessAccounts }}',
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
  - name: bucket
    props:
      - name: BucketName
        value: '{{ BucketName }}'
      - name: BundleId
        value: '{{ BundleId }}'
      - name: ObjectVersioning
        value: '{{ ObjectVersioning }}'
      - name: AccessRules
        value:
          GetObject: '{{ GetObject }}'
          AllowPublicOverrides: '{{ AllowPublicOverrides }}'
      - name: ResourcesReceivingAccess
        value:
          - '{{ ResourcesReceivingAccess[0] }}'
      - name: ReadOnlyAccessAccounts
        value:
          - '{{ ReadOnlyAccessAccounts[0] }}'
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

### Read
```json
lightsail:GetBuckets
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

### Update
```json
lightsail:GetBuckets,
lightsail:GetInstance,
lightsail:UpdateBucket,
lightsail:UpdateBucketBundle,
lightsail:SetResourceAccessForBucket,
lightsail:TagResource,
lightsail:UntagResource
```

