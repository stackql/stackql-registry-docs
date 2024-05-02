---
title: access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point
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
Gets or operates on an individual <code>access_point</code> resource, use <code>access_points</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessPoint resource is an Amazon S3 resource type that you can use to access buckets.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.access_point</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name you want to assign to this Access Point. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the access point name.</td></tr>
<tr><td><code>alias</code></td><td><code>string</code></td><td>The alias of this Access Point. This alias can be used for compatibility purposes with other AWS services and third-party applications.</td></tr>
<tr><td><code>bucket</code></td><td><code>string</code></td><td>The name of the bucket that you want to associate this Access Point with.</td></tr>
<tr><td><code>bucket_account_id</code></td><td><code>string</code></td><td>The AWS account ID associated with the S3 bucket associated with this access point.</td></tr>
<tr><td><code>vpc_configuration</code></td><td><code>object</code></td><td>If you include this field, Amazon S3 restricts access to this Access Point to requests from the specified Virtual Private Cloud (VPC).</td></tr>
<tr><td><code>public_access_block_configuration</code></td><td><code>object</code></td><td>The PublicAccessBlock configuration that you want to apply to this Access Point. You can enable the configuration options in any combination. For more information about when Amazon S3 considers a bucket or object public, see https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;access-control-block-public-access.html#access-control-block-public-access-policy-status 'The Meaning of Public' in the Amazon Simple Storage Service Developer Guide.</td></tr>
<tr><td><code>policy</code></td><td><code>object</code></td><td>The Access Point Policy you want to apply to this access point.</td></tr>
<tr><td><code>network_origin</code></td><td><code>string</code></td><td>Indicates whether this Access Point allows access from the public Internet. If VpcConfiguration is specified for this Access Point, then NetworkOrigin is VPC, and the Access Point doesn't allow access from the public Internet. Otherwise, NetworkOrigin is Internet, and the Access Point allows access from the public Internet, subject to the Access Point and bucket access policies.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified accesspoint.</td></tr>
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
name,
alias,
bucket,
bucket_account_id,
vpc_configuration,
public_access_block_configuration,
policy,
network_origin,
arn
FROM aws.s3.access_point
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>access_point</code> resource, the following permissions are required:

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

