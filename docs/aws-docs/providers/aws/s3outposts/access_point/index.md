---
title: access_point
hide_title: false
hide_table_of_contents: false
keywords:
  - access_point
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

Gets or operates on an individual <code>access_point</code> resource, use <code>access_points</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for AWS::S3Outposts::AccessPoint</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3outposts.access_point" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified AccessPoint.</td></tr>
<tr><td><CopyableCode code="bucket" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the bucket you want to associate this AccessPoint with.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name for the AccessPoint.</td></tr>
<tr><td><CopyableCode code="vpc_configuration" /></td><td><code>object</code></td><td>Virtual Private Cloud (VPC) from which requests can be made to the AccessPoint.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>The access point policy associated with this access point.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
bucket,
name,
vpc_configuration,
policy
FROM aws.s3outposts.access_point
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>access_point</code> resource, the following permissions are required:

### Read
```json
s3-outposts:GetAccessPoint,
s3-outposts:GetAccessPointPolicy
```

### Update
```json
s3-outposts:GetAccessPoint,
s3-outposts:PutAccessPointPolicy,
s3-outposts:GetAccessPointPolicy,
s3-outposts:DeleteAccessPointPolicy
```

### Delete
```json
s3-outposts:DeleteAccessPoint,
s3-outposts:DeleteAccessPointPolicy
```

