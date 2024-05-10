---
title: access_grants_instance
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_instance
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


Gets or updates an individual <code>access_grants_instance</code> resource, use <code>access_grants_instances</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_instance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrantsInstance resource is an Amazon S3 resource type that hosts Access Grants and their associated locations</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grants_instance" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_grants_instance_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified Access Grants instance.</td></tr>
<tr><td><CopyableCode code="identity_center_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the specified AWS Identity Center.</td></tr>
<tr><td><CopyableCode code="access_grants_instance_id" /></td><td><code>string</code></td><td>A unique identifier for the specified access grants instance.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
access_grants_instance_arn,
identity_center_arn,
access_grants_instance_id,
tags
FROM aws.s3.access_grants_instance
WHERE region = 'us-east-1' AND data__Identifier = '<AccessGrantsInstanceArn>';
```


## Permissions

To operate on the <code>access_grants_instance</code> resource, the following permissions are required:

### Read
```json
s3:GetAccessGrantsInstance
```

### Update
```json
s3:TagResource
```

