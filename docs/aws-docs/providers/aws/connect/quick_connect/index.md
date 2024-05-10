---
title: quick_connect
hide_title: false
hide_table_of_contents: false
keywords:
  - quick_connect
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


Gets or updates an individual <code>quick_connect</code> resource, use <code>quick_connects</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quick_connect</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::QuickConnect</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.quick_connect" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the quick connect.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the quick connect.</td></tr>
<tr><td><CopyableCode code="quick_connect_config" /></td><td><code>object</code></td><td>Configuration settings for the quick connect.</td></tr>
<tr><td><CopyableCode code="quick_connect_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the quick connect.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="quick_connect_type" /></td><td><code>string</code></td><td>The type of quick connect. In the Amazon Connect console, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).</td></tr>
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
instance_arn,
name,
description,
quick_connect_config,
quick_connect_arn,
tags,
quick_connect_type
FROM aws.connect.quick_connect
WHERE region = 'us-east-1' AND data__Identifier = '<QuickConnectArn>';
```


## Permissions

To operate on the <code>quick_connect</code> resource, the following permissions are required:

### Read
```json
connect:DescribeQuickConnect
```

### Update
```json
connect:UpdateQuickConnectName,
connect:UpdateQuickConnectConfig,
connect:TagResource,
connect:UntagResource
```

