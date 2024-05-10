---
title: location_efs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_efs
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


Gets or updates an individual <code>location_efs</code> resource, use <code>location_efs</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_efs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationEFS.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_efs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="ec2_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="efs_filesystem_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Amazon EFS file system.</td></tr>
<tr><td><CopyableCode code="access_point_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Amazon EFS Access point that DataSync uses when accessing the EFS file system.</td></tr>
<tr><td><CopyableCode code="file_system_access_role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AWS IAM role that the DataSync will assume when mounting the EFS file system.</td></tr>
<tr><td><CopyableCode code="in_transit_encryption" /></td><td><code>string</code></td><td>Protocol that is used for encrypting the traffic exchanged between the DataSync Agent and the EFS file system.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>A subdirectory in the location's path. This subdirectory in the EFS file system is used to read data from the EFS source location or write data to the EFS destination.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the EFS location that was described.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
ec2_config,
efs_filesystem_arn,
access_point_arn,
file_system_access_role_arn,
in_transit_encryption,
subdirectory,
tags,
location_arn,
location_uri
FROM aws.datasync.location_efs
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```


## Permissions

To operate on the <code>location_efs</code> resource, the following permissions are required:

### Read
```json
datasync:DescribeLocationEfs,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationEfs,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource
```

