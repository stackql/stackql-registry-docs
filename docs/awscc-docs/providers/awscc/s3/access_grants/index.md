---
title: access_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants
  - s3
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>access_grants</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>access_grants</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.s3.access_grants</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>access_grant_id</code></td><td><code>string</code></td><td>The ID assigned to this access grant.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>access_grants</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessGrant,
s3:TagResource
```

### List
```json
s3:ListAccessGrants
```


## Example
```sql
SELECT
region,
access_grant_id
FROM awscc.s3.access_grants
WHERE region = 'us-east-1'
```
