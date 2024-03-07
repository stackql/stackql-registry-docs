---
title: fhir_datastore
hide_title: false
hide_table_of_contents: false
keywords:
  - fhir_datastore
  - healthlake
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>fhir_datastore</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_datastore</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fhir_datastore</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.healthlake.fhir_datastore</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>created_at</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>datastore_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_endpoint</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>datastore_type_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>preload_data_config</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>sse_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>identity_provider_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
created_at,
datastore_arn,
datastore_endpoint,
datastore_id,
datastore_name,
datastore_status,
datastore_type_version,
preload_data_config,
sse_configuration,
identity_provider_configuration,
tags
FROM awscc.healthlake.fhir_datastore
WHERE region = 'us-east-1'
AND data__Identifier = '{DatastoreId}';
```

## Permissions

To operate on the <code>fhir_datastore</code> resource, the following permissions are required:

### Read
```json
healthlake:DescribeFHIRDatastore,
healthlake:ListTagsForResource
```

### Update
```json
healthlake:TagResource,
healthlake:UntagResource,
healthlake:ListTagsForResource,
healthlake:DescribeFHIRDatastore,
iam:PassRole,
iam:GetRole,
iam:CreateServiceLinkedRole
```

### Delete
```json
healthlake:DeleteFHIRDatastore,
healthlake:DescribeFHIRDatastore,
iam:PassRole,
iam:GetRole,
iam:CreateServiceLinkedRole,
ram:GetResourceShareInvitations,
ram:AcceptResourceShareInvitation,
glue:CreateDatabase,
glue:DeleteDatabase
```

