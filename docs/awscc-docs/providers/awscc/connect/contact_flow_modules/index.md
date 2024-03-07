---
title: contact_flow_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_flow_modules
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
Retrieves a list of <code>contact_flow_modules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flow_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>contact_flow_modules</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.connect.contact_flow_modules</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>contact_flow_module_arn</code></td><td><code>string</code></td><td>The identifier of the contact flow module (ARN).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>contact_flow_modules</code> resource, the following permissions are required:

### Create
```json
connect:CreateContactFlowModule,
connect:TagResource
```

### List
```json
connect:ListContactFlowModules
```


## Example
```sql
SELECT
region,
contact_flow_module_arn
FROM awscc.connect.contact_flow_modules
WHERE region = 'us-east-1'
```
