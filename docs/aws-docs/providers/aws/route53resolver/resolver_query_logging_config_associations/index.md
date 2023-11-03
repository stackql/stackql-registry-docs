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
Retrieves a list of <code>resolver_query_logging_config_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_config_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_query_logging_config_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>Id</td></tr><tr><td><code>ResolverQueryLogConfigId</code></td><td><code>string</code></td><td>ResolverQueryLogConfigId</td></tr><tr><td><code>ResourceId</code></td><td><code>string</code></td><td>ResourceId</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationStatus</td></tr><tr><td><code>Error</code></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationError</td></tr><tr><td><code>ErrorMessage</code></td><td><code>string</code></td><td>ResolverQueryLogConfigAssociationErrorMessage</td></tr><tr><td><code>CreationTime</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53resolver.resolver_query_logging_config_associations
WHERE region = 'us-east-1'
</pre>
