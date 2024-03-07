---
title: datastore
hide_title: false
hide_table_of_contents: false
keywords:
  - datastore
  - healthimaging
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>datastore</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datastore</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>datastore</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.healthimaging.datastore</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>datastore_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>datastore</code> resource, the following permissions are required:

### Read
```json
medical-imaging:GetDatastore,
medical-imaging:ListTagsForResource
```

### Delete
```json
medical-imaging:DeleteDatastore,
medical-imaging:GetDatastore,
medical-imaging:UntagResource,
kms:DescribeKey,
kms:RetireGrant,
kms:GenerateDataKey,
kms:Decrypt
```


## Example
```sql
SELECT
region,
datastore_arn,
datastore_name,
datastore_id,
datastore_status,
kms_key_arn,
created_at,
updated_at,
tags
FROM awscc.healthimaging.datastore
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DatastoreId&gt;'
```
