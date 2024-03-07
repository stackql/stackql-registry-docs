---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
  - refactorspaces
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.refactorspaces.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>network_fabric_type</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>transit_gateway_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
```json
refactor-spaces:GetEnvironment,
refactor-spaces:ListTagsForResource
```

### Delete
```json
refactor-spaces:GetEnvironment,
refactor-spaces:DeleteEnvironment,
refactor-spaces:UntagResource,
ec2:DescribeTransitGateways,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:DeleteTransitGateway,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:DeleteTags,
ram:GetResourceShareAssociations,
ram:DeleteResourceShare
```


## Example
```sql
SELECT
region,
description,
environment_identifier,
name,
network_fabric_type,
arn,
transit_gateway_id,
tags
FROM awscc.refactorspaces.environment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;EnvironmentIdentifier&gt;'
```
