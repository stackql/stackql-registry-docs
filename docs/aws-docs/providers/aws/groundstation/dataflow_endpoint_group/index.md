---
title: dataflow_endpoint_group
hide_title: false
hide_table_of_contents: false
keywords:
  - dataflow_endpoint_group
  - groundstation
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

Gets or operates on an individual <code>dataflow_endpoint_group</code> resource, use <code>dataflow_endpoint_groups</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dataflow_endpoint_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station DataflowEndpointGroup schema for CloudFormation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.groundstation.dataflow_endpoint_group" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_details" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="contact_pre_pass_duration_seconds" /></td><td><code>integer</code></td><td>Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a PREPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the PREPASS state.</td></tr>
<tr><td><CopyableCode code="contact_post_pass_duration_seconds" /></td><td><code>integer</code></td><td>Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a POSTPASS state. A Ground Station Dataflow Endpoint Group State Change event will be emitted when the Dataflow Endpoint Group enters and exits the POSTPASS state.</td></tr>
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
id,
arn,
endpoint_details,
contact_pre_pass_duration_seconds,
contact_post_pass_duration_seconds,
tags
FROM aws.groundstation.dataflow_endpoint_group
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>dataflow_endpoint_group</code> resource, the following permissions are required:

### Read
```json
groundstation:GetDataflowEndpointGroup,
groundstation:ListTagsForResource
```

### Delete
```json
groundstation:DeleteDataflowEndpointGroup,
groundstation:GetDataflowEndpointGroup
```

