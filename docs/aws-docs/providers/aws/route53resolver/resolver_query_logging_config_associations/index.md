---
title: resolver_query_logging_config_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_query_logging_config_associations
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

Creates, updates, deletes or gets a <code>resolver_query_logging_config_association</code> resource or lists <code>resolver_query_logging_config_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_config_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_query_logging_config_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><CopyableCode code="resolver_query_log_config_id" /></td><td><code>string</code></td><td>ResolverQueryLogConfigId</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationStatus</td></tr>
<tr><td><CopyableCode code="error" /></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationError</td></tr>
<tr><td><CopyableCode code="error_message" /></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationErrorMessage</td></tr>
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
Gets all <code>resolver_query_logging_config_associations</code> in a region.
```sql
SELECT
region,
id,
resolver_query_log_config_id,
resource_id,
status,
error,
error_message,
creation_time
FROM aws.route53resolver.resolver_query_logging_config_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resolver_query_logging_config_association</code>.
```sql
SELECT
region,
id,
resolver_query_log_config_id,
resource_id,
status,
error,
error_message,
creation_time
FROM aws.route53resolver.resolver_query_logging_config_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resolver_query_logging_config_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.route53resolver.resolver_query_logging_config_associations (
 ResolverQueryLogConfigId,
 ResourceId,
 region
)
SELECT 
'{{ ResolverQueryLogConfigId }}',
 '{{ ResourceId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.route53resolver.resolver_query_logging_config_associations (
 ResolverQueryLogConfigId,
 ResourceId,
 region
)
SELECT 
 '{{ ResolverQueryLogConfigId }}',
 '{{ ResourceId }}',
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
  - name: resolver_query_logging_config_association
    props:
      - name: ResolverQueryLogConfigId
        value: '{{ ResolverQueryLogConfigId }}'
      - name: ResourceId
        value: '{{ ResourceId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.route53resolver.resolver_query_logging_config_associations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resolver_query_logging_config_associations</code> resource, the following permissions are required:

### Create
```json
resolverquerylogging:AssociateConfig,
resolverquerylogging:GetConfigAssociation,
route53resolver:AssociateResolverQueryLogConfig,
ec2:DescribeVpcs,
route53resolver:GetResolverQueryLogConfigAssociation
```

### Read
```json
resolverquerylogging:GetConfigAssociation,
route53resolver:GetResolverQueryLogConfigAssociation
```

### Delete
```json
resolverquerylogging:DisassociateConfig,
resolverquerylogging:ListConfigAssociation,
route53resolver:DisassociateResolverQueryLogConfig,
route53resolver:ListResolverQueryLogConfigAssociations,
route53resolver:GetResolverQueryLogConfigAssociation
```

### List
```json
resolverquerylogging:ListConfigAssociations,
route53resolver:ListResolverQueryLogConfigAssociations
```

