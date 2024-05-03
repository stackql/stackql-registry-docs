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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>contact_flow_modules</code> in a region or create a <code>contact_flow_modules</code> resource, use <code>contact_flow_module</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_flow_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ContactFlowModule.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.contact_flow_modules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="contact_flow_module_arn" /></td><td><code>string</code></td><td>The identifier of the contact flow module (ARN).</td></tr>
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
contact_flow_module_arn
FROM aws.connect.contact_flow_modules
WHERE region = 'us-east-1'
```

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

