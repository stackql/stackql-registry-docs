---
title: location_azure_blob
hide_title: false
hide_table_of_contents: false
keywords:
  - location_azure_blob
  - datasync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>location_azure_blob</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_azure_blob</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>location_azure_blob</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datasync.location_azure_blob</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>agent_arns</code></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.</td></tr>
<tr><td><code>azure_blob_authentication_type</code></td><td><code>string</code></td><td>The specific authentication type that you want DataSync to use to access your Azure Blob Container.</td></tr>
<tr><td><code>azure_blob_sas_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>azure_blob_container_url</code></td><td><code>string</code></td><td>The URL of the Azure Blob container that was described.</td></tr>
<tr><td><code>azure_blob_type</code></td><td><code>string</code></td><td>Specifies a blob type for the objects you're transferring into your Azure Blob Storage container.</td></tr>
<tr><td><code>azure_access_tier</code></td><td><code>string</code></td><td>Specifies an access tier for the objects you're transferring into your Azure Blob Storage container.</td></tr>
<tr><td><code>subdirectory</code></td><td><code>string</code></td><td>The subdirectory in the Azure Blob Container that is used to read data from the Azure Blob Source Location.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>location_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Azure Blob Location that is created.</td></tr>
<tr><td><code>location_uri</code></td><td><code>string</code></td><td>The URL of the Azure Blob Location that was described.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>location_azure_blob</code> resource, the following permissions are required:

### Read
<pre>
datasync:DescribeLocationAzureBlob,
datasync:ListTagsForResource</pre>

### Update
<pre>
datasync:DescribeLocationAzureBlob,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
datasync:UpdateLocationAzureBlob</pre>

### Delete
<pre>
datasync:DeleteLocation</pre>


## Example
```sql
SELECT
region,
agent_arns,
azure_blob_authentication_type,
azure_blob_sas_configuration,
azure_blob_container_url,
azure_blob_type,
azure_access_tier,
subdirectory,
tags,
location_arn,
location_uri
FROM awscc.datasync.location_azure_blob
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;LocationArn&gt;'
```
