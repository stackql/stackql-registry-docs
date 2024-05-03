---
title: transit_gateway_connect
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_connect
  - ec2
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

Gets or operates on an individual <code>transit_gateway_connect</code> resource, use <code>transit_gateway_connects</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_connect</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayConnect type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_connect" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the Connect attachment.</td></tr>
<tr><td><CopyableCode code="transport_transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the attachment from which the Connect attachment was created.</td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the attachment.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>The creation time.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the attachment.</td></tr>
<tr><td><CopyableCode code="options" /></td><td><code>object</code></td><td>The Connect attachment options.</td></tr>
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
transit_gateway_attachment_id,
transport_transit_gateway_attachment_id,
transit_gateway_id,
state,
creation_time,
tags,
options
FROM aws.ec2.transit_gateway_connect
WHERE data__Identifier = '<TransitGatewayAttachmentId>';
```

## Permissions

To operate on the <code>transit_gateway_connect</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeTransitGatewayConnects
```

### Update
```json
ec2:DescribeTransitGatewayConnects,
ec2:DeleteTags,
ec2:CreateTags
```

### Delete
```json
ec2:DeleteTransitGatewayConnect,
ec2:DescribeTransitGatewayConnects,
ec2:DeleteTags
```
