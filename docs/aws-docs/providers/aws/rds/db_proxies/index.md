---
title: db_proxies
hide_title: false
hide_table_of_contents: false
keywords:
  - db_proxies
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


Used to retrieve a list of <code>db_proxies</code> in a region or to create or delete a <code>db_proxies</code> resource, use <code>db_proxy</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxies" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_proxy_name" /></td><td><code>string</code></td><td>The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.</td></tr>
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
db_proxy_name
FROM aws.rds.db_proxies
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>db_proxy</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- db_proxy.iql (required properties only)
INSERT INTO aws.rds.db_proxies (
 Auth,
 DBProxyName,
 EngineFamily,
 RoleArn,
 VpcSubnetIds,
 region
)
SELECT 
'{{ Auth }}',
 '{{ DBProxyName }}',
 '{{ EngineFamily }}',
 '{{ RoleArn }}',
 '{{ VpcSubnetIds }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- db_proxy.iql (all properties)
INSERT INTO aws.rds.db_proxies (
 Auth,
 DBProxyName,
 DebugLogging,
 EngineFamily,
 IdleClientTimeout,
 RequireTLS,
 RoleArn,
 Tags,
 VpcSecurityGroupIds,
 VpcSubnetIds,
 region
)
SELECT 
 '{{ Auth }}',
 '{{ DBProxyName }}',
 '{{ DebugLogging }}',
 '{{ EngineFamily }}',
 '{{ IdleClientTimeout }}',
 '{{ RequireTLS }}',
 '{{ RoleArn }}',
 '{{ Tags }}',
 '{{ VpcSecurityGroupIds }}',
 '{{ VpcSubnetIds }}',
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
  - name: db_proxy
    props:
      - name: Auth
        value:
          - AuthScheme: '{{ AuthScheme }}'
            Description: '{{ Description }}'
            IAMAuth: '{{ IAMAuth }}'
            SecretArn: '{{ SecretArn }}'
            ClientPasswordAuthType: '{{ ClientPasswordAuthType }}'
      - name: DBProxyName
        value: '{{ DBProxyName }}'
      - name: DebugLogging
        value: '{{ DebugLogging }}'
      - name: EngineFamily
        value: '{{ EngineFamily }}'
      - name: IdleClientTimeout
        value: '{{ IdleClientTimeout }}'
      - name: RequireTLS
        value: '{{ RequireTLS }}'
      - name: RoleArn
        value: '{{ RoleArn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: VpcSecurityGroupIds
        value:
          - '{{ VpcSecurityGroupIds[0] }}'
      - name: VpcSubnetIds
        value:
          - '{{ VpcSubnetIds[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.rds.db_proxies
WHERE data__Identifier = '<DBProxyName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>db_proxies</code> resource, the following permissions are required:

### Create
```json
rds:CreateDBProxy,
rds:DescribeDBProxies,
iam:PassRole
```

### Delete
```json
rds:DescribeDBProxies,
rds:DeleteDBProxy
```

### List
```json
rds:DescribeDBProxies
```

