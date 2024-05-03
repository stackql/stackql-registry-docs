---
title: endpoint
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoint
  - events
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

Gets or operates on an individual <code>endpoint</code> resource, use <code>endpoints</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoint</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.endpoint" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="routing_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="replication_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="event_buses" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state_reason" /></td><td><code>string</code></td><td></td></tr>
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
name,
arn,
role_arn,
description,
routing_config,
replication_config,
event_buses,
endpoint_id,
endpoint_url,
state,
state_reason
FROM aws.events.endpoint
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>endpoint</code> resource, the following permissions are required:

### Read
```json
events:DescribeEndpoint
```

### Update
```json
events:DescribeEndpoint,
events:UpdateEndpoint,
route53:GetHealthCheck,
iam:PassRole
```

### Delete
```json
events:DeleteEndpoint,
events:DescribeEndpoint
```

