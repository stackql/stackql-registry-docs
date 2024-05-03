---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - codeconnections
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

Used to retrieve a list of <code>connections</code> in a region or create a <code>connections</code> resource, use <code>connection</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for AWS::CodeConnections::Connection resource which can be used to connect external source providers with other AWS services (i.e. AWS CodePipeline)</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codeconnections.connections" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="connection_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the  connection. The ARN is used as the connection reference when the connection is shared between AWS services.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
connection_arn
FROM aws.codeconnections.connections
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>connections</code> resource, the following permissions are required:

### Create
```json
codeconnections:CreateConnection,
codeconnections:TagResource
```

### List
```json
codeconnections:ListConnections,
codeconnections:ListTagsForResource
```
