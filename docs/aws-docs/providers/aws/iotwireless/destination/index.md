---
title: destination
hide_title: false
hide_table_of_contents: false
keywords:
  - destination
  - iotwireless
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


Gets or updates an individual <code>destination</code> resource, use <code>destinations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destination</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Destination's resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotwireless.destination" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Unique name of destination</td></tr>
<tr><td><CopyableCode code="expression" /></td><td><code>string</code></td><td>Destination expression</td></tr>
<tr><td><CopyableCode code="expression_type" /></td><td><code>string</code></td><td>Must be RuleName</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Destination description</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the destination.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>AWS role ARN that grants access</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Destination arn. Returned after successful create.</td></tr>
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
name,
expression,
expression_type,
description,
tags,
role_arn,
arn
FROM aws.iotwireless.destination
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```


## Permissions

To operate on the <code>destination</code> resource, the following permissions are required:

### Read
```json
iotwireless:GetDestination,
iotwireless:ListTagsForResource
```

### Update
```json
iam:PassRole,
iotwireless:UpdateDestination,
iotwireless:UntagResource,
iotwireless:ListTagsForResource
```

