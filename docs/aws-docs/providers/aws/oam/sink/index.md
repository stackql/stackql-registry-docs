---
title: sink
hide_title: false
hide_table_of_contents: false
keywords:
  - sink
  - oam
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

Gets or operates on an individual <code>sink</code> resource, use <code>sinks</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sink</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Oam::Sink</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.oam.sink" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) of the ObservabilityAccessManager Sink</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the ObservabilityAccessManager Sink.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td>The policy of this ObservabilityAccessManager Sink.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>Tags to apply to the sink</td></tr>
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
name,
policy,
tags
FROM aws.oam.sink
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>sink</code> resource, the following permissions are required:

### Delete
```json
oam:DeleteSink,
oam:GetSinkPolicy,
oam:GetSink
```

### Read
```json
oam:GetSinkPolicy,
oam:GetSink
```

### Update
```json
oam:PutSinkPolicy,
oam:GetSinkPolicy,
oam:GetSink,
oam:TagResource,
oam:UntagResource
```

