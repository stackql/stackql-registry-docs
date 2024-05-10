---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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


Used to retrieve a list of <code>applications</code> in a region or to create or delete a <code>applications</code> resource, use <code>application</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Application Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
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
environment_identifier,
application_identifier
FROM aws.refactorspaces.applications
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- application.iql (required properties only)
INSERT INTO aws.refactorspaces.applications (
 EnvironmentIdentifier,
 Name,
 ProxyType,
 VpcId,
 region
)
SELECT 
'{{ EnvironmentIdentifier }}',
 '{{ Name }}',
 '{{ ProxyType }}',
 '{{ VpcId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- application.iql (all properties)
INSERT INTO aws.refactorspaces.applications (
 ApiGatewayProxy,
 EnvironmentIdentifier,
 Name,
 ProxyType,
 VpcId,
 Tags,
 region
)
SELECT 
 '{{ ApiGatewayProxy }}',
 '{{ EnvironmentIdentifier }}',
 '{{ Name }}',
 '{{ ProxyType }}',
 '{{ VpcId }}',
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
  - name: application
    props:
      - name: ApiGatewayProxy
        value:
          StageName: '{{ StageName }}'
          EndpointType: '{{ EndpointType }}'
      - name: EnvironmentIdentifier
        value: '{{ EnvironmentIdentifier }}'
      - name: Name
        value: '{{ Name }}'
      - name: ProxyType
        value: '{{ ProxyType }}'
      - name: VpcId
        value: '{{ VpcId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.refactorspaces.applications
WHERE data__Identifier = '<EnvironmentIdentifier|ApplicationIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
refactor-spaces:GetApplication,
refactor-spaces:CreateApplication,
refactor-spaces:TagResource,
ec2:CreateTags,
ec2:CreateVpcEndpointServiceConfiguration,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:DescribeAccountAttributes,
ec2:DescribeInternetGateways,
ec2:ModifyVpcEndpointServicePermissions,
apigateway:DELETE,
apigateway:GET,
apigateway:PATCH,
apigateway:POST,
apigateway:PUT,
apigateway:UpdateRestApiPolicy,
apigateway:Update*,
apigateway:Delete*,
apigateway:Get*,
apigateway:Put*,
elasticloadbalancing:CreateLoadBalancer,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DescribeTags,
elasticloadbalancing:AddTags,
iam:CreateServiceLinkedRole
```

### Delete
```json
refactor-spaces:GetApplication,
refactor-spaces:DeleteApplication,
refactor-spaces:UntagResource,
ec2:DescribeVpcEndpointServiceConfigurations,
ec2:DeleteRoute,
ec2:DeleteSecurityGroup,
ec2:DeleteTransitGateway,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:DeleteVpcEndpointServiceConfigurations,
ec2:DeleteTags,
ec2:RevokeSecurityGroupIngress,
elasticloadbalancing:DeleteLoadBalancer,
apigateway:Update*,
apigateway:Delete*,
apigateway:Get*,
apigateway:Put*
```

### List
```json
refactor-spaces:ListApplications,
refactor-spaces:ListTagsForResource
```

