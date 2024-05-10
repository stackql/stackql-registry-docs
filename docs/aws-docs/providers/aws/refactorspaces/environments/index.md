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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>environments</code> in a region or to create or delete a <code>environments</code> resource, use <code>environment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Environment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
environment_identifier
FROM aws.refactorspaces.environments
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>environment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- environment.iql (required properties only)
INSERT INTO aws.refactorspaces.environments (
 Name,
 NetworkFabricType,
 region
)
SELECT 
'{{ Name }}',
 '{{ NetworkFabricType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- environment.iql (all properties)
INSERT INTO aws.refactorspaces.environments (
 Description,
 Name,
 NetworkFabricType,
 Tags,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ NetworkFabricType }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: environment
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: NetworkFabricType
        value: '{{ NetworkFabricType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.refactorspaces.environments
WHERE data__Identifier = '<EnvironmentIdentifier>'
AND region = 'us-east-1';
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

### List
```json
refactor-spaces:ListEnvironments,
refactor-spaces:ListTagsForResource
```

