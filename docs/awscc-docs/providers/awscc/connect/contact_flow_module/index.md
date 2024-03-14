---
title: contact_flow_module
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_flow_module
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
Gets an individual <code>contact_flow_module</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flow_module</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>contact_flow_module</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.contact_flow_module</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>instance_arn</code></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance (ARN).</td></tr>
<tr><td><code>contact_flow_module_arn</code></td><td><code>string</code></td><td>The identifier of the contact flow module (ARN).</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the contact flow module.</td></tr>
<tr><td><code>content</code></td><td><code>string</code></td><td>The content of the contact flow module in JSON format.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the contact flow module.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the contact flow module.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the contact flow module.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
instance_arn,
contact_flow_module_arn,
name,
content,
description,
state,
status,
tags
FROM awscc.connect.contact_flow_module
WHERE data__Identifier = '<ContactFlowModuleArn>';
```

## Permissions

To operate on the <code>contact_flow_module</code> resource, the following permissions are required:

### Read
```json
connect:DescribeContactFlowModule
```

### Delete
```json
connect:DeleteContactFlowModule,
connect:UntagResource
```

### Update
```json
connect:UpdateContactFlowModuleMetadata,
connect:UpdateContactFlowModuleContent,
connect:TagResource,
connect:UntagResource
```

