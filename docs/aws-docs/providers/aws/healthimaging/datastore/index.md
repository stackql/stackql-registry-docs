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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>datastore</code> resource, use <code>datastores</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datastore</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::HealthImaging::Datastore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.healthimaging.datastore" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="datastore_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
datastore_arn,
datastore_name,
datastore_id,
datastore_status,
kms_key_arn,
created_at,
updated_at,
tags
FROM aws.healthimaging.datastore
WHERE data__Identifier = '<DatastoreId>';
```

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

