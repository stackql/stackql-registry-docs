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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>environment</code> resource, use <code>environments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Environment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.environment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="network_fabric_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="transit_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
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
description,
environment_identifier,
name,
network_fabric_type,
arn,
transit_gateway_id,
tags
FROM aws.refactorspaces.environment
WHERE data__Identifier = '<EnvironmentIdentifier>';
```

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

