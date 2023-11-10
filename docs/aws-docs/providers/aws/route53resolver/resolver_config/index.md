---
title: resolver_config
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver_config
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
Gets an individual <code>resolver_config</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver_config</td></tr>
<tr><td><b>Id</b></td><td><code>aws.route53resolver.resolver_config</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>owner_id</code></td><td><code>string</code></td><td>AccountId</td></tr>
<tr><td><code>resource_id</code></td><td><code>string</code></td><td>ResourceId</td></tr>
<tr><td><code>autodefined_reverse</code></td><td><code>string</code></td><td>ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.</td></tr>
<tr><td><code>autodefined_reverse_flag</code></td><td><code>string</code></td><td>Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
owner_id,
resource_id,
autodefined_reverse,
autodefined_reverse_flag
FROM aws.route53resolver.resolver_config
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
