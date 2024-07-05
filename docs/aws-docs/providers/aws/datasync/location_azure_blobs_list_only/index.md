---
title: location_azure_blobs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - location_azure_blobs_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>location_azure_blobs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/location_azure_blobs/"><code>location_azure_blobs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_azure_blobs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationAzureBlob.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_azure_blobs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.</td></tr>
<tr><td><CopyableCode code="azure_blob_authentication_type" /></td><td><code>string</code></td><td>The specific authentication type that you want DataSync to use to access your Azure Blob Container.</td></tr>
<tr><td><CopyableCode code="azure_blob_sas_configuration" /></td><td><code>object</code></td><td>Specifies the shared access signature (SAS) that DataSync uses to access your Azure Blob Storage container.</td></tr>
<tr><td><CopyableCode code="azure_blob_container_url" /></td><td><code>string</code></td><td>The URL of the Azure Blob container that was described.</td></tr>
<tr><td><CopyableCode code="azure_blob_type" /></td><td><code>string</code></td><td>Specifies a blob type for the objects you're transferring into your Azure Blob Storage container.</td></tr>
<tr><td><CopyableCode code="azure_access_tier" /></td><td><code>string</code></td><td>Specifies an access tier for the objects you're transferring into your Azure Blob Storage container.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>The subdirectory in the Azure Blob Container that is used to read data from the Azure Blob Source Location.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Azure Blob Location that is created.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the Azure Blob Location that was described.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>location_azure_blobs</code> in a region.
```sql
SELECT
region,
location_arn
FROM aws.datasync.location_azure_blobs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>location_azure_blobs_list_only</code> resource, see <a href="/providers/aws/datasync/location_azure_blobs/#permissions"><code>location_azure_blobs</code></a>


