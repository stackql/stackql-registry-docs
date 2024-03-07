---
title: data_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_integrations
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
Retrieves a list of <code>data_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>data_integrations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appintegrations.data_integrations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifer of the data integration.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>data_integrations</code> resource, the following permissions are required:

### Create
<pre>
app-integrations:CreateDataIntegration,
app-integrations:TagResource,
appflow:DescribeConnectorProfiles,
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
kms:ListKeys,
s3:GetBucketNotification,
s3:PutBucketNotification,
s3:GetEncryptionConfiguration</pre>

### List
<pre>
app-integrations:ListDataIntegrations</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.appintegrations.data_integrations
WHERE region = 'us-east-1'
```
