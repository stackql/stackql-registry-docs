---
title: flow_entitlements
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_entitlements
  - mediaconnect
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

Used to retrieve a list of <code>flow_entitlements</code> in a region or create a <code>flow_entitlements</code> resource, use <code>flow_entitlement</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_entitlements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaConnect::FlowEntitlement</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediaconnect.flow_entitlements" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="entitlement_arn" /></td><td><code>string</code></td><td>The ARN of the entitlement.</td></tr>
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
entitlement_arn
FROM aws.mediaconnect.flow_entitlements
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>flow_entitlements</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
mediaconnect:GrantFlowEntitlements
```

### List
```json
mediaconnect:DescribeFlow
```

