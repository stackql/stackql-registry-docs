---
title: instance
hide_title: false
hide_table_of_contents: false
keywords:
  - instance
  - connect
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


Gets or updates an individual <code>instance</code> resource, use <code>instances</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::Instance</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.instance" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>An instanceId is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>An instanceArn is automatically generated on creation based on instanceId.</td></tr>
<tr><td><CopyableCode code="identity_management_type" /></td><td><code>string</code></td><td>Specifies the type of directory integration for new instance.</td></tr>
<tr><td><CopyableCode code="instance_alias" /></td><td><code>string</code></td><td>Alias of the new directory created as part of new instance creation.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>Timestamp of instance creation logged as part of instance creation.</td></tr>
<tr><td><CopyableCode code="service_role" /></td><td><code>string</code></td><td>Service linked role created as part of instance creation.</td></tr>
<tr><td><CopyableCode code="instance_status" /></td><td><code>string</code></td><td>Specifies the creation status of new instance.</td></tr>
<tr><td><CopyableCode code="directory_id" /></td><td><code>string</code></td><td>Existing directoryId user wants to map to the new Connect instance.</td></tr>
<tr><td><CopyableCode code="attributes" /></td><td><code>object</code></td><td>The attributes for the instance.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
id,
arn,
identity_management_type,
instance_alias,
created_time,
service_role,
instance_status,
directory_id,
attributes,
tags
FROM aws.connect.instance
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


## Permissions

To operate on the <code>instance</code> resource, the following permissions are required:

### Read
```json
connect:DescribeInstance,
connect:ListInstanceAttributes,
ds:DescribeDirectories
```

### Update
```json
connect:ListInstanceAttributes,
connect:UpdateInstanceAttribute,
iam:CreateServiceLinkedRole,
iam:PutRolePolicy,
connect:TagResource,
connect:UntagResource
```

