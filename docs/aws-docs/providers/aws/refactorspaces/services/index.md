---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Used to retrieve a list of <code>services</code> in a region or create a <code>services</code> resource, use <code>service</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Service Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
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
environment_identifier,
application_identifier,
service_identifier
FROM aws.refactorspaces.services
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
```json
refactor-spaces:CreateService,
refactor-spaces:GetService,
refactor-spaces:TagResource,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeRouteTables,
ec2:CreateTags,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateSecurityGroup,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateRoute,
lambda:GetFunctionConfiguration
```

### List
```json
refactor-spaces:ListServices,
refactor-spaces:ListTagsForResource
```

