---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
  - xray
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


Gets or updates an individual <code>group</code> resource, use <code>groups</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This schema provides construct and validation rules for AWS-XRay Group resource parameters.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.xray.group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="filter_expression" /></td><td><code>string</code></td><td>The filter expression defining criteria by which to group traces.</td></tr>
<tr><td><CopyableCode code="group_name" /></td><td><code>string</code></td><td>The case-sensitive name of the new group. Names must be unique.</td></tr>
<tr><td><CopyableCode code="group_arn" /></td><td><code>string</code></td><td>The ARN of the group that was generated on creation.</td></tr>
<tr><td><CopyableCode code="insights_configuration" /></td><td><code>object</code></td><td></td></tr>
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
filter_expression,
group_name,
group_arn,
insights_configuration,
tags
FROM aws.xray.group
WHERE region = 'us-east-1' AND data__Identifier = '<GroupARN>';
```


## Permissions

To operate on the <code>group</code> resource, the following permissions are required:

### Read
```json
xray:GetGroup,
xray:ListTagsForResource
```

### Update
```json
xray:UpdateGroup,
xray:TagResource,
xray:UntagResource,
xray:ListTagsForResource
```

