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

Creates, updates, deletes or gets an <code>environment</code> resource or lists <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Environment Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.environments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, NetworkFabricType, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>environments</code> in a region.
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
FROM aws.refactorspaces.environments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>environment</code>.
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
FROM aws.refactorspaces.environments
WHERE region = 'us-east-1' AND data__Identifier = '<EnvironmentIdentifier>';
```

## `INSERT` example

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
/*+ create */
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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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

### List
```json
refactor-spaces:ListEnvironments,
refactor-spaces:ListTagsForResource
```

