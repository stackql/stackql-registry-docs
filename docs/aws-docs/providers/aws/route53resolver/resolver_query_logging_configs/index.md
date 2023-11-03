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
Retrieves a list of <code>resolver_query_logging_configs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_query_logging_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_query_logging_configs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td>ResourceId</td></tr><tr><td><code>OwnerId</code></td><td><code>string</code></td><td>AccountId</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.</td></tr><tr><td><code>ShareStatus</code></td><td><code>string</code></td><td>ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.</td></tr><tr><td><code>AssociationCount</code></td><td><code>integer</code></td><td>Count</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Arn</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>ResolverQueryLogConfigName</td></tr><tr><td><code>CreatorRequestId</code></td><td><code>string</code></td><td>The id of the creator request.</td></tr><tr><td><code>DestinationArn</code></td><td><code>string</code></td><td>destination arn</td></tr><tr><td><code>CreationTime</code></td><td><code>string</code></td><td>Rfc3339TimeString</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.route53resolver.resolver_query_logging_configs
WHERE region = 'us-east-1'
</pre>
