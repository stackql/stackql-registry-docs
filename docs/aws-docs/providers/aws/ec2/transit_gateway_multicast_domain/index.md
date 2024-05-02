---
title: transit_gateway_multicast_domain
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domain
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
Gets or operates on an individual <code>transit_gateway_multicast_domain</code> resource, use <code>transit_gateway_multicast_domains</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domain</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastDomain type</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.transit_gateway_multicast_domain</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>transit_gateway_multicast_domain_id</code></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><code>transit_gateway_multicast_domain_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the transit gateway multicast domain.</td></tr>
<tr><td><code>transit_gateway_id</code></td><td><code>string</code></td><td>The ID of the transit gateway.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the transit gateway multicast domain.</td></tr>
<tr><td><code>creation_time</code></td><td><code>string</code></td><td>The time the transit gateway multicast domain was created.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the transit gateway multicast domain.</td></tr>
<tr><td><code>options</code></td><td><code>object</code></td><td>The options for the transit gateway multicast domain.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
transit_gateway_multicast_domain_id,
transit_gateway_multicast_domain_arn,
transit_gateway_id,
state,
creation_time,
tags,
options
FROM aws.ec2.transit_gateway_multicast_domain
WHERE data__Identifier = '<TransitGatewayMulticastDomainId>';
```

## Permissions

To operate on the <code>transit_gateway_multicast_domain</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeTransitGatewayMulticastDomains
```

### Update
```json
ec2:DescribeTransitGatewayMulticastDomains,
ec2:DeleteTags,
ec2:CreateTags
```

### Delete
```json
ec2:DescribeTransitGatewayMulticastDomains,
ec2:DeleteTransitGatewayMulticastDomain,
ec2:DeleteTags
```

