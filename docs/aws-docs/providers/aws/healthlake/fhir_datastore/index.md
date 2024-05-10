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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>fhir_datastore</code> resource, use <code>fhir_datastores</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fhir_datastore</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>HealthLake FHIR Datastore</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.healthlake.fhir_datastore" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_endpoint" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="datastore_type_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="preload_data_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="sse_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.healthlake.fhir_datastore
WHERE region = 'us-east-1' AND data__Identifier = '<DatastoreId>';
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

