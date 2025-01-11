---
title: db_proxy_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxy_endpoints
  - rds
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

Creates, updates, deletes or gets a <code>db_proxy_endpoint</code> resource or lists <code>db_proxy_endpoints</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxyEndpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="db_proxy_endpoint_name" /></td><td><code>string</code></td><td>The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><CopyableCode code="db_proxy_endpoint_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="db_proxy_name" /></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td>VPC ID to associate with the new DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_security_group_ids" /></td><td><code>array</code></td><td>VPC security group IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="vpc_subnet_ids" /></td><td><code>array</code></td><td>VPC subnet IDs to associate with the new DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint" /></td><td><code>string</code></td><td>The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.</td></tr>
<tr><td><CopyableCode code="target_role" /></td><td><code>string</code></td><td>A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td>A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbproxyendpoint.html"><code>AWS::RDS::DBProxyEndpoint</code></a>.

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
    <td><CopyableCode code="DBProxyName, DBProxyEndpointName, VpcSubnetIds, region" /></td>
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
Gets all <code>db_proxy_endpoints</code> in a region.
```sql
SELECT
region,
db_proxy_endpoint_name,
db_proxy_endpoint_arn,
db_proxy_name,
vpc_id,
vpc_security_group_ids,
vpc_subnet_ids,
endpoint,
target_role,
is_default,
tags
FROM aws.rds.db_proxy_endpoints
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>db_proxy_endpoint</code>.
```sql
SELECT
region,
db_proxy_endpoint_name,
db_proxy_endpoint_arn,
db_proxy_name,
vpc_id,
vpc_security_group_ids,
vpc_subnet_ids,
endpoint,
target_role,
is_default,
tags
FROM aws.rds.db_proxy_endpoints
WHERE region = 'us-east-1' AND data__Identifier = '<DBProxyEndpointName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>db_proxy_endpoint</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.rds.db_proxy_endpoints (
 DBProxyEndpointName,
 DBProxyName,
 VpcSubnetIds,
 region
)
SELECT 
'{{ DBProxyEndpointName }}',
 '{{ DBProxyName }}',
 '{{ VpcSubnetIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.rds.db_proxy_endpoints (
 DBProxyEndpointName,
 DBProxyName,
 VpcSecurityGroupIds,
 VpcSubnetIds,
 TargetRole,
 Tags,
 region
)
SELECT 
 '{{ DBProxyEndpointName }}',
 '{{ DBProxyName }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ VpcSubnetIds }}',
 '{{ TargetRole }}',
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
  - name: db_proxy_endpoint
    props:
      - name: DBProxyEndpointName
        value: '{{ DBProxyEndpointName }}'
      - name: DBProxyName
        value: '{{ DBProxyName }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'
      - name: VpcSubnetIds
        value:
          - '{{ VpcSubnetIds[0] }}'
      - name: TargetRole
        value: '{{ TargetRole }}'
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
DELETE FROM aws.rds.db_proxy_endpoints
WHERE data__Identifier = '<DBProxyEndpointName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_proxy_endpoints</code> resource, the following permissions are required:

### Create
```json
rds:CreateDBProxyEndpoint,
rds:DescribeDBProxyEndpoints
```

### Read
```json
rds:DescribeDBProxyEndpoints,
rds:ListTagsForResource
```

### Update
```json
rds:ModifyDBProxyEndpoint,
rds:AddTagsToResource,
rds:RemoveTagsFromResource
```

### Delete
```json
rds:DescribeDBProxyEndpoints,
rds:DeleteDBProxyEndpoint
```

### List
```json
rds:DescribeDBProxyEndpoints
```
