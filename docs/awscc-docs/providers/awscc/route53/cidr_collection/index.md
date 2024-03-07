---
title: cidr_collection
hide_title: false
hide_table_of_contents: false
keywords:
  - cidr_collection
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
Gets an individual <code>cidr_collection</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cidr_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>cidr_collection</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.route53.cidr_collection</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>UUID of the CIDR collection.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A unique name for the CIDR collection.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon resource name (ARN) to uniquely identify the AWS resource.</td></tr>
<tr><td><code>locations</code></td><td><code>array</code></td><td>A complex type that contains information about the list of CIDR locations.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
name,
arn,
locations
FROM awscc.route53.cidr_collection
WHERE data__Identifier = '{Id}';
```

## Permissions

To operate on the <code>cidr_collection</code> resource, the following permissions are required:

### Read
```json
route53:ListCidrCollections,
route53:ListCidrBlocks
```

### Update
```json
route53:ChangeCidrCollection
```

### Delete
```json
route53:DeleteCidrCollection,
route53:ChangeCidrCollection
```

