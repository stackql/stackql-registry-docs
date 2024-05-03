---
title: data_integration
hide_title: false
hide_table_of_contents: false
keywords:
  - data_integration
  - appintegrations
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

Gets or operates on an individual <code>data_integration</code> resource, use <code>data_integrations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::DataIntegration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.data_integration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The data integration description.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifer of the data integration.</td></tr>
<tr><td><CopyableCode code="data_integration_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the data integration.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the data integration.</td></tr>
<tr><td><CopyableCode code="kms_key" /></td><td><code>string</code></td><td>The KMS key of the data integration.</td></tr>
<tr><td><CopyableCode code="schedule_config" /></td><td><code>object</code></td><td>The name of the data and how often it should be pulled from the source.</td></tr>
<tr><td><CopyableCode code="source_uri" /></td><td><code>string</code></td><td>The URI of the data source.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the data integration.</td></tr>
<tr><td><CopyableCode code="file_configuration" /></td><td><code>object</code></td><td>The configuration for what files should be pulled from the source.</td></tr>
<tr><td><CopyableCode code="object_configuration" /></td><td><code>object</code></td><td>The configuration for what data should be pulled from the source.</td></tr>
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
description,
id,
data_integration_arn,
name,
kms_key,
schedule_config,
source_uri,
tags,
file_configuration,
object_configuration
FROM aws.appintegrations.data_integration
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>data_integration</code> resource, the following permissions are required:

### Read
```json
app-integrations:GetDataIntegration,
app-integrations:ListTagsForResource
```

### Update
```json
app-integrations:GetDataIntegration,
app-integrations:UpdateDataIntegration,
app-integrations:TagResource,
app-integrations:UntagResource,
appflow:DescribeConnectorProfiles,
appflow:DeleteFlow,
appflow:DescribeConnectorEntity,
appflow:UseConnectorProfile,
appflow:TagResource,
appflow:UntagResource,
kms:CreateGrant,
kms:DescribeKey,
kms:ListAliases,
kms:ListGrants,
kms:ListKeys
```

### Delete
```json
app-integrations:DeleteDataIntegration,
app-integrations:UntagResource,
appflow:CreateFlow,
appflow:DeleteFlow,
appflow:DescribeConnectorEntity,
appflow:UseConnectorProfile,
appflow:TagResource,
appflow:UntagResource,
kms:CreateGrant,
kms:DescribeKey,
kms:ListAliases,
kms:ListGrants,
kms:ListKeys
```

