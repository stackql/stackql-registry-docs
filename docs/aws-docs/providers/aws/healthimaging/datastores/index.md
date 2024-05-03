---
title: datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - datastores
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

Used to retrieve a list of <code>datastores</code> in a region or create a <code>datastores</code> resource, use <code>datastore</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::HealthImaging::Datastore Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.healthimaging.datastores" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="datastore_id" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
datastore_id
FROM aws.healthimaging.datastores
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>datastores</code> resource, the following permissions are required:

### Create
```json
medical-imaging:CreateDatastore,
medical-imaging:GetDatastore,
kms:DescribeKey,
kms:CreateGrant,
kms:RetireGrant,
kms:GenerateDataKey,
kms:Decrypt,
lambda:InvokeFunction,
medical-imaging:TagResource,
medical-imaging:UntagResource,
medical-imaging:ListTagsForResource
```

### List
```json
medical-imaging:ListDatastores
```
