---
title: vpc_links
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_links
  - apigatewayv2
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

Creates, updates, deletes or gets a <code>vpc_link</code> resource or lists <code>vpc_links</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::ApiGatewayV2::VpcLink</code> resource creates a VPC link. Supported only for HTTP APIs. The VPC link status must transition from <code>PENDING</code> to <code>AVAILABLE</code> to successfully create a VPC link, which can take up to 10 minutes. To learn more, see &#91;Working with VPC Links for HTTP APIs&#93;(https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html) in the *API Gateway Developer Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apigatewayv2.vpc_links" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="vpc_link_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="subnet_ids" /></td><td><code>array</code></td><td>A list of subnet IDs to include in the VPC link.</td></tr>
<tr><td><CopyableCode code="security_group_ids" /></td><td><code>array</code></td><td>A list of security group IDs for the VPC link.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>The collection of tags. Each tag element is associated with a given resource.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the VPC link.</td></tr>
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
    <td><CopyableCode code="SubnetIds, Name, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>vpc_links</code> in a region.
```sql
SELECT
region,
vpc_link_id
FROM aws.apigatewayv2.vpc_links
WHERE region = 'us-east-1';
```
Gets all properties from a <code>vpc_link</code>.
```sql
SELECT
region,
vpc_link_id,
subnet_ids,
security_group_ids,
tags,
name
FROM aws.apigatewayv2.vpc_links
WHERE region = 'us-east-1' AND data__Identifier = '<VpcLinkId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>vpc_link</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apigatewayv2.vpc_links (
 SubnetIds,
 Name,
 region
)
SELECT 
'{{ SubnetIds }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apigatewayv2.vpc_links (
 SubnetIds,
 SecurityGroupIds,
 Tags,
 Name,
 region
)
SELECT 
 '{{ SubnetIds }}',
 '{{ SecurityGroupIds }}',
 '{{ Tags }}',
 '{{ Name }}',
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
  - name: vpc_link
    props:
      - name: SubnetIds
        value:
          - '{{ SubnetIds[0] }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: Tags
        value: {}
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apigatewayv2.vpc_links
WHERE data__Identifier = '<VpcLinkId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>vpc_links</code> resource, the following permissions are required:

### Create
```json
apigateway:POST,
apigateway:GET,
apigateway:TagResource,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Update
```json
apigateway:PATCH,
apigateway:GET,
apigateway:TagResource,
apigateway:unTagResource,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Read
```json
apigateway:GET,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### Delete
```json
apigateway:GET,
apigateway:DELETE,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

### List
```json
apigateway:GET,
iam:CreateServiceLinkedRole,
iam:DeleteServiceLinkedRole,
iam:GetServiceLinkedRoleDeletionStatus
```

