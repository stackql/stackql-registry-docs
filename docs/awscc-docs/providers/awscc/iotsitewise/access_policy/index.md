---
title: access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy
  - iotsitewise
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>access_policy</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_policy</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotsitewise.access_policy</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_policy_id</code></td><td><code>string</code></td><td>The ID of the access policy.</td></tr>
<tr><td><code>access_policy_arn</code></td><td><code>string</code></td><td>The ARN of the access policy.</td></tr>
<tr><td><code>access_policy_identity</code></td><td><code>object</code></td><td>The identity for this access policy. Choose either a user or a group but not both.</td></tr>
<tr><td><code>access_policy_permission</code></td><td><code>string</code></td><td>The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.</td></tr>
<tr><td><code>access_policy_resource</code></td><td><code>object</code></td><td>The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
access_policy_id,
access_policy_arn,
access_policy_identity,
access_policy_permission,
access_policy_resource
FROM awscc.iotsitewise.access_policy
WHERE data__Identifier = '<AccessPolicyId>';
```

## Permissions

To operate on the <code>access_policy</code> resource, the following permissions are required:

### Read
```json
iotsitewise:DescribeAccessPolicy
```

### Update
```json
iotsitewise:DescribeAccessPolicy,
iotsitewise:UpdateAccessPolicy
```

### Delete
```json
iotsitewise:DescribeAccessPolicy,
iotsitewise:DeleteAccessPolicy
```

