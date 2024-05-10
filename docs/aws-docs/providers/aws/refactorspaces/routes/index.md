---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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


Used to retrieve a list of <code>routes</code> in a region or to create or delete a <code>routes</code> resource, use <code>route</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Route Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.routes" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="route_identifier" /></td><td><code>string</code></td><td></td></tr>
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
application_identifier,
route_identifier
FROM aws.refactorspaces.routes
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>route</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- route.iql (required properties only)
INSERT INTO aws.refactorspaces.routes (
 ApplicationIdentifier,
 EnvironmentIdentifier,
 RouteType,
 ServiceIdentifier,
 region
)
SELECT 
'{{ ApplicationIdentifier }}',
 '{{ EnvironmentIdentifier }}',
 '{{ RouteType }}',
 '{{ ServiceIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- route.iql (all properties)
INSERT INTO aws.refactorspaces.routes (
 ApplicationIdentifier,
 EnvironmentIdentifier,
 RouteType,
 ServiceIdentifier,
 DefaultRoute,
 UriPathRoute,
 Tags,
 region
)
SELECT 
 '{{ ApplicationIdentifier }}',
 '{{ EnvironmentIdentifier }}',
 '{{ RouteType }}',
 '{{ ServiceIdentifier }}',
 '{{ DefaultRoute }}',
 '{{ UriPathRoute }}',
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
  - name: route
    props:
      - name: ApplicationIdentifier
        value: '{{ ApplicationIdentifier }}'
      - name: EnvironmentIdentifier
        value: '{{ EnvironmentIdentifier }}'
      - name: RouteType
        value: '{{ RouteType }}'
      - name: ServiceIdentifier
        value: '{{ ServiceIdentifier }}'
      - name: DefaultRoute
        value:
          ActivationState: '{{ ActivationState }}'
      - name: UriPathRoute
        value:
          SourcePath: '{{ SourcePath }}'
          ActivationState: null
          Methods:
            - '{{ Methods[0] }}'
          IncludeChildPaths: '{{ IncludeChildPaths }}'
          AppendSourcePath: '{{ AppendSourcePath }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.refactorspaces.routes
WHERE data__Identifier = '<EnvironmentIdentifier|ApplicationIdentifier|RouteIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>routes</code> resource, the following permissions are required:

### Create
```json
refactor-spaces:CreateRoute,
refactor-spaces:GetRoute,
refactor-spaces:TagResource,
iam:CreateServiceLinkedRole,
apigateway:GET,
apigateway:PATCH,
apigateway:POST,
apigateway:PUT,
apigateway:DELETE,
apigateway:UpdateRestApiPolicy,
lambda:GetFunctionConfiguration,
lambda:AddPermission,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeTargetGroups,
elasticloadbalancing:CreateListener,
elasticloadbalancing:CreateTargetGroup,
elasticloadbalancing:DescribeTags,
elasticloadbalancing:AddTags,
elasticloadbalancing:RegisterTargets,
elasticloadbalancing:DescribeTargetHealth,
ec2:DescribeSubnets,
tag:GetResources
```

### Delete
```json
refactor-spaces:DeleteRoute,
refactor-spaces:GetRoute,
refactor-spaces:UntagResource,
apigateway:GET,
apigateway:PATCH,
apigateway:POST,
apigateway:PUT,
apigateway:DELETE,
apigateway:UpdateRestApiPolicy,
lambda:GetFunctionConfiguration,
lambda:AddPermission,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeTargetGroups,
elasticloadbalancing:CreateListener,
elasticloadbalancing:CreateTargetGroup,
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DeleteTargetGroup,
elasticloadbalancing:DescribeTags,
elasticloadbalancing:AddTags,
elasticloadbalancing:RegisterTargets,
elasticloadbalancing:DescribeTargetHealth,
ec2:DescribeSubnets,
tag:GetResources
```

### List
```json
refactor-spaces:ListRoutes,
refactor-spaces:ListTagsForResource
```

