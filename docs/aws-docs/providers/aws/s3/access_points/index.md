---
title: access_points
hide_title: false
hide_table_of_contents: false
keywords:
  - access_points
  - s3
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

Creates, updates, deletes or gets an <code>access_point</code> resource or lists <code>access_points</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_points" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.</td></tr>
<tr><td><CopyableCode code="bucket" /></td><td><code>string</code></td><td>The name of the bucket that you want to associate this Access Point with.</td></tr>
<tr><td><CopyableCode code="bucket_account_id" /></td><td><code>string</code></td><td>The AWS account ID associated with the S3 bucket associated with this access point.</td></tr>
<tr><td><CopyableCode code="vpc_configuration" /></td><td><code>object</code></td><td>If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).</td></tr>
<tr><td><CopyableCode code="public_access_block_configuration" /></td><td><code>object</code></td><td>The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>The Access Point Policy you want to apply to this access point.</td></tr>
<tr><td><CopyableCode code="network_origin" /></td><td><code>string</code></td><td>Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified accesspoint.</td></tr>
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
    <td><CopyableCode code="Bucket, region" /></td>
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
Gets all <code>access_points</code> in a region.
```sql
SELECT
region,
name,
alias,
bucket,
bucket_account_id,
vpc_configuration,
public_access_block_configuration,
policy,
network_origin,
arn
FROM aws.s3.access_points
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>access_point</code>.
```sql
SELECT
region,
name,
alias,
bucket,
bucket_account_id,
vpc_configuration,
public_access_block_configuration,
policy,
network_origin,
arn
FROM aws.s3.access_points
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>access_point</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.s3.access_points (
 Bucket,
 region
)
SELECT 
'{{ Bucket }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.s3.access_points (
 Name,
 Bucket,
 BucketAccountId,
 VpcConfiguration,
 PublicAccessBlockConfiguration,
 Policy,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Bucket }}',
 '{{ BucketAccountId }}',
 '{{ VpcConfiguration }}',
 '{{ PublicAccessBlockConfiguration }}',
 '{{ Policy }}',
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
  - name: access_point
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Bucket
        value: '{{ Bucket }}'
      - name: BucketAccountId
        value: '{{ BucketAccountId }}'
      - name: VpcConfiguration
        value:
          VpcId: '{{ VpcId }}'
      - name: PublicAccessBlockConfiguration
        value:
          BlockPublicAcls: '{{ BlockPublicAcls }}'
          IgnorePublicAcls: '{{ IgnorePublicAcls }}'
          BlockPublicPolicy: '{{ BlockPublicPolicy }}'
          RestrictPublicBuckets: '{{ RestrictPublicBuckets }}'
      - name: Policy
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.s3.access_points
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>access_points</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessPoint,
s3:PutAccessPointPolicy,
s3:PutAccessPointPublicAccessBlock
```

### Read
```json
s3:GetAccessPoint,
s3:GetAccessPointPolicy
```

### Update
```json
s3:PutAccessPointPolicy,
s3:PutAccessPointPublicAccessBlock,
s3:DeleteAccessPointPolicy,
s3:GetAccessPoint,
s3:GetAccessPointPolicy
```

### Delete
```json
s3:DeleteAccessPointPolicy,
s3:DeleteAccessPoint
```

### List
```json
s3:ListAccessPoints
```

