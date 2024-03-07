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
Gets an individual <code>data_integration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_integration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appintegrations.data_integration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The data integration description.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifer of the data integration.</td></tr>
<tr><td><code>data_integration_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the data integration.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the data integration.</td></tr>
<tr><td><code>kms_key</code></td><td><code>string</code></td><td>The KMS key of the data integration.</td></tr>
<tr><td><code>schedule_config</code></td><td><code>object</code></td><td>The name of the data and how often it should be pulled from the source.</td></tr>
<tr><td><code>source_ur_i</code></td><td><code>string</code></td><td>The URI of the data source.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the data integration.</td></tr>
<tr><td><code>file_configuration</code></td><td><code>object</code></td><td>The configuration for what files should be pulled from the source.</td></tr>
<tr><td><code>object_configuration</code></td><td><code>object</code></td><td>The configuration for what data should be pulled from the source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

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


## Example
```sql
SELECT
region,
description,
id,
data_integration_arn,
name,
kms_key,
schedule_config,
source_ur_i,
tags,
file_configuration,
object_configuration
FROM awscc.appintegrations.data_integration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
