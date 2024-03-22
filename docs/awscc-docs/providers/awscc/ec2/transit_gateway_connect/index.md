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
Gets an individual <code>transit_gateway_connect</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_connect</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>transit_gateway_connect</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ec2.transit_gateway_connect</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>transit_gateway_attachment_id</code></td><td><code>string</code></td><td>The ID of the Connect attachment.</td></tr>
<tr><td><code>transport_transit_gateway_attachment_id</code></td><td><code>string</code></td><td>The ID of the attachment from which the Connect attachment was created.</td></tr>
<tr><td><code>transit_gateway_id</code></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the attachment.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The creation time.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the attachment.</td></tr>
<tr><td><code>options</code></td><td><code>object</code></td><td>The Connect attachment options.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.ec2.transit_gateway_connect
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

