---
title: contact_flow
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_flow
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

Gets or operates on an individual <code>contact_flow</code> resource, use <code>contact_flows</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ContactFlow</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.contact_flow" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance (ARN).</td></tr>
<tr><td><CopyableCode code="contact_flow_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow (ARN).</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the contact flow.</td></tr>
<tr><td><CopyableCode code="content" /></td><td><code>string</code></td><td>The content of the contact flow in JSON format.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the contact flow.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the contact flow.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the contact flow.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
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
instance_arn,
contact_flow_arn,
name,
content,
description,
state,
type,
tags
FROM aws.connect.contact_flow
WHERE data__Identifier = '<ContactFlowArn>';
```

## Permissions

To operate on the <code>contact_flow</code> resource, the following permissions are required:

### Read
```json
connect:DescribeContactFlow
```

### Delete
```json
connect:DeleteContactFlow,
connect:UntagResource
```

### Update
```json
connect:UpdateContactFlowMetadata,
connect:UpdateContactFlowContent,
connect:TagResource,
connect:UntagResource
```

