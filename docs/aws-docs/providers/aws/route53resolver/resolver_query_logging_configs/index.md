---
title: resolver_query_logging_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_query_logging_configs
  - route53resolver
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


Used to retrieve a list of <code>resolver_query_logging_configs</code> in a region or to create or delete a <code>resolver_query_logging_configs</code> resource, use <code>resolver_query_logging_config</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_query_logging_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
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
id
FROM aws.route53resolver.resolver_query_logging_configs
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
 "Name": "{{ Name }}",
 "DestinationArn": "{{ DestinationArn }}"
}
>>>
--required properties only
INSERT INTO aws.route53resolver.resolver_query_logging_configs (
 Name,
 DestinationArn,
 region
)
SELECT 
{{ .Name }},
 {{ .DestinationArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "Name": "{{ Name }}",
 "DestinationArn": "{{ DestinationArn }}"
}
>>>
--all properties
INSERT INTO aws.route53resolver.resolver_query_logging_configs (
 Name,
 DestinationArn,
 region
)
SELECT 
 {{ .Name }},
 {{ .DestinationArn }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.route53resolver.resolver_query_logging_configs
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resolver_query_logging_configs</code> resource, the following permissions are required:

### Create
```json
resolverquerylogging:CreateConfig,
resolverquerylogging:GetConfig,
route53resolver:CreateResolverQueryLogConfig,
route53resolver:GetResolverQueryLogConfig,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups,
iam:CreateServiceLinkedRole
```

### Delete
```json
resolverquerylogging:DeleteConfig,
resolverquerylogging:ListConfig,
route53resolver:DeleteResolverQueryLogConfig,
route53resolver:ListResolverQueryLogConfigs
```

### List
```json
resolverquerylogging:ListConfig,
route53resolver:ListResolverQueryLogConfigs
```

