---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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
Retrieves a list of <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environments</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.refactorspaces.environments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>environment_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
environment_identifier
FROM awscc.refactorspaces.environments
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>environments</code> resource, the following permissions are required:

### Create
```json
refactor-spaces:CreateEnvironment,
refactor-spaces:GetEnvironment,
refactor-spaces:TagResource,
ec2:CreateTransitGateway,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateSecurityGroup,
ec2:CreateTags,
ec2:DescribeNetworkInterfaces,
ec2:DescribeRouteTables,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:DescribeTags,
ec2:DescribeTransitGateways,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:ModifyVpcEndpointServicePermissions,
ec2:RevokeSecurityGroupIngress,
ram:AssociateResourceShare,
ram:CreateResourceShare,
ram:GetResourceShareAssociations,
ram:GetResourceShares,
ram:TagResource,
ram:GetResourceShareInvitations,
ram:AcceptResourceShareInvitation,
ram:DisassociateResourceShare,
tag:GetResources,
iam:CreateServiceLinkedRole
```

### List
```json
refactor-spaces:ListEnvironments,
refactor-spaces:ListTagsForResource
```

