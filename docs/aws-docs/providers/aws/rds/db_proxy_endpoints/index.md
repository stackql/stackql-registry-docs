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


Used to retrieve a list of <code>db_proxy_endpoints</code> in a region or to create or delete a <code>db_proxy_endpoints</code> resource, use <code>db_proxy_endpoint</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>db_proxy_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::RDS::DBProxyEndpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.db_proxy_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="db_proxy_endpoint_name" /></td><td><code>string</code></td><td>The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.</td></tr>
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
db_proxy_endpoint_name
FROM aws.rds.db_proxy_endpoints
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "DBProxyEndpointName": "{{ DBProxyEndpointName }}",
 "DBProxyName": "{{ DBProxyName }}",
 "VpcSubnetIds": [
  "{{ VpcSubnetIds[0] }}"
 ]
}
>>>
--required properties only
INSERT INTO aws.rds.db_proxy_endpoints (
 DBProxyEndpointName,
 DBProxyName,
 VpcSubnetIds,
 region
)
SELECT 
{{ DBProxyEndpointName }},
 {{ DBProxyName }},
 {{ VpcSubnetIds }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "DBProxyEndpointName": "{{ DBProxyEndpointName }}",
 "DBProxyName": "{{ DBProxyName }}",
 "VpcSecurityGroupIds": [
  "{{ VpcSecurityGroupIds[0] }}"
 ],
 "VpcSubnetIds": [
  "{{ VpcSubnetIds[0] }}"
 ],
 "TargetRole": "{{ TargetRole }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
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
 {{ DBProxyEndpointName }},
 {{ DBProxyName }},
 {{ VpcSecurityGroupIds }},
 {{ VpcSubnetIds }},
 {{ TargetRole }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
rds:DescribeDBProxyEndpoints,
rds:DeleteDBProxyEndpoint
```

### List
```json
rds:DescribeDBProxyEndpoints
```

