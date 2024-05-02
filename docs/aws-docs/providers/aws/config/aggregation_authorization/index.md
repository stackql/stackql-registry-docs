---
title: aggregation_authorization
hide_title: false
hide_table_of_contents: false
keywords:
  - aggregation_authorization
  - config
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>aggregation_authorization</code> resource, use <code>aggregation_authorizations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>aggregation_authorization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::AggregationAuthorization</td></tr>
<tr><td><b>Id</b></td><td><code>aws.config.aggregation_authorization</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>authorized_account_id</code></td><td><code>string</code></td><td>The 12-digit account ID of the account authorized to aggregate data.</td></tr>
<tr><td><code>authorized_aws_region</code></td><td><code>string</code></td><td>The region authorized to collect aggregated data.</td></tr>
<tr><td><code>aggregation_authorization_arn</code></td><td><code>string</code></td><td>The ARN of the AggregationAuthorization.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the AggregationAuthorization.</td></tr>
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
authorized_account_id,
authorized_aws_region,
aggregation_authorization_arn,
tags
FROM aws.config.aggregation_authorization
WHERE data__Identifier = '<AuthorizedAccountId>|<AuthorizedAwsRegion>';
```

## Permissions

To operate on the <code>aggregation_authorization</code> resource, the following permissions are required:

### Update
```json
config:DescribeAggregationAuthorizations,
config:TagResource,
config:UntagResource,
config:ListTagsForResource
```

### Read
```json
config:DescribeAggregationAuthorizations,
config:ListTagsForResource
```

### Delete
```json
config:DescribeAggregationAuthorizations,
config:DeleteAggregationAuthorization,
config:UntagResource
```

