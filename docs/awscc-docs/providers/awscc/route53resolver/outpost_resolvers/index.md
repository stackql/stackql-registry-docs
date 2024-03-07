---
title: outpost_resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - outpost_resolvers
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
Retrieves a list of <code>outpost_resolvers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>outpost_resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>outpost_resolvers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53resolver.outpost_resolvers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Id</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id
FROM awscc.route53resolver.outpost_resolvers
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>outpost_resolvers</code> resource, the following permissions are required:

### Create
```json
route53resolver:CreateOutpostResolver,
route53resolver:GetOutpostResolver,
route53resolver:ListTagsForResource,
outposts:GetOutpost
```

### List
```json
route53resolver:ListOutpostResolvers,
route53resolver:ListTagsForResource
```

