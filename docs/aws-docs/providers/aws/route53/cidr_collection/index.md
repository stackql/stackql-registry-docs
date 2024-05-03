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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>cidr_collection</code> resource, use <code>cidr_collections</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cidr_collection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Route53::CidrCollection.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53.cidr_collection" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>UUID of the CIDR collection.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A unique name for the CIDR collection.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon resource name (ARN) to uniquely identify the AWS resource.</td></tr>
<tr><td><CopyableCode code="locations" /></td><td><code>array</code></td><td>A complex type that contains information about the list of CIDR locations.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
name,
arn,
locations
FROM aws.route53.cidr_collection
WHERE data__Identifier = '<Id>';
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

