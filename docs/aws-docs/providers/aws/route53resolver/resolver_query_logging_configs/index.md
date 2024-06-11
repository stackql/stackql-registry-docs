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

Creates, updates, deletes or gets a <code>resolver_query_logging_config</code> resource or lists <code>resolver_query_logging_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfig.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_query_logging_configs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="owner_id" /></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.</td></tr>
<tr><td><CopyableCode code="share_status" /></td><td><code>string</code></td><td>ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.</td></tr>
<tr><td><CopyableCode code="association_count" /></td><td><code>integer</code></td><td>Count</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Arn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>ResolverQueryLogConfigName</td></tr>
<tr><td><CopyableCode code="creator_request_id" /></td><td><code>string</code></td><td>The id of the creator request.</td></tr>
<tr><td><CopyableCode code="destination_arn" /></td><td><code>string</code></td><td>destination arn</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
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
    <td><CopyableCode code="region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>resolver_query_logging_configs</code> in a region.
```sql
SELECT
region,
id
FROM aws.route53resolver.resolver_query_logging_configs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>resolver_query_logging_config</code>.
```sql
SELECT
region,
id,
owner_id,
status,
share_status,
association_count,
arn,
name,
creator_request_id,
destination_arn,
creation_time
FROM aws.route53resolver.resolver_query_logging_configs
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resolver_query_logging_config</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53resolver.resolver_query_logging_configs (
 Name,
 DestinationArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ DestinationArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53resolver.resolver_query_logging_configs (
 Name,
 DestinationArn,
 region
)
SELECT 
 '{{ Name }}',
 '{{ DestinationArn }}',
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
  - name: resolver_query_logging_config
    props:
      - name: Name
        value: '{{ Name }}'
      - name: DestinationArn
        value: '{{ DestinationArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
resolverquerylogging:GetConfig,
route53resolver:GetResolverQueryLogConfig
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

