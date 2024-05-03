---
title: resolver_query_logging_config_association
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_query_logging_config_association
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

Gets or operates on an individual <code>resolver_query_logging_config_association</code> resource, use <code>resolver_query_logging_config_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_config_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53Resolver::ResolverQueryLoggingConfigAssociation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53resolver.resolver_query_logging_config_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.route53resolver.resolver_query_logging_config_association
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>resolver_query_logging_config_association</code> resource, the following permissions are required:

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

