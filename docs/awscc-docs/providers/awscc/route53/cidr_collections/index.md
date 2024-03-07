---
title: cidr_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - cidr_collections
  - route53
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>cidr_collections</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cidr_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cidr_collections</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.cidr_collections</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>UUID of the CIDR collection.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>cidr_collections</code> resource, the following permissions are required:

### Create
<pre>
route53:CreateCidrCollection,
route53:ChangeCidrCollection</pre>

### List
<pre>
route53:ListCidrCollections,
route53:ListCidrBlocks</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.route53.cidr_collections

```
