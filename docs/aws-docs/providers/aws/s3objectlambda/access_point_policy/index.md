---
title: access_point_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point_policy
  - s3objectlambda
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_point_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS::S3ObjectLambda::AccessPointPolicy resource is an Amazon S3ObjectLambda policy type that you can use to control permissions for your S3ObjectLambda</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3objectlambda.access_point_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>object_lambda_access_point</code></td><td><code>string</code></td><td>The name of the Amazon S3 ObjectLambdaAccessPoint to which the policy applies.</td></tr>
<tr><td><code>policy_document</code></td><td><code>object</code></td><td>A policy document containing permissions to add to the specified ObjectLambdaAccessPoint. For more information, see Access Policy Language Overview (https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AmazonS3&#x2F;latest&#x2F;dev&#x2F;access-policy-language-overview.html) in the Amazon Simple Storage Service Developer Guide. </td></tr>
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
object_lambda_access_point,
policy_document
FROM aws.s3objectlambda.access_point_policy
WHERE data__Identifier = '<ObjectLambdaAccessPoint>';
```

## Permissions

To operate on the <code>access_point_policy</code> resource, the following permissions are required:

### Read
```json
s3:GetAccessPointPolicyForObjectLambda
```

### Update
```json
s3:PutAccessPointPolicyForObjectLambda,
s3:GetAccessPointPolicyForObjectLambda
```

### Delete
```json
s3:DeleteAccessPointPolicyForObjectLambda,
s3:GetAccessPointPolicyForObjectLambda
```

