---
title: location_azure_blobs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_azure_blobs
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

Creates, updates, deletes or gets a <code>location_azure_blob</code> resource or lists <code>location_azure_blobs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_azure_blobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationAzureBlob.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_azure_blobs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="agent_arns" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of agents to use for an Azure Blob Location.</td></tr>
<tr><td><CopyableCode code="azure_blob_authentication_type" /></td><td><code>string</code></td><td>The specific authentication type that you want DataSync to use to access your Azure Blob Container.</td></tr>
<tr><td><CopyableCode code="azure_blob_sas_configuration" /></td><td><code>Specifies the shared access signature (SAS) that DataSync uses to access your Azure Blob Storage container.</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="AzureBlobAuthenticationType, AgentArns, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>location_azure_blobs</code> in a region.
```sql
SELECT
region,
location_arn
FROM aws.datasync.location_azure_blobs
WHERE region = 'us-east-1';
```
Gets all properties from a <code>location_azure_blob</code>.
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
FROM aws.datasync.location_azure_blobs
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>location_azure_blob</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.datasync.location_azure_blobs (
 AgentArns,
 AzureBlobAuthenticationType,
 region
)
SELECT 
'{{ AgentArns }}',
 '{{ AzureBlobAuthenticationType }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.location_azure_blobs (
 AgentArns,
 AzureBlobAuthenticationType,
 AzureBlobSasConfiguration,
 AzureBlobContainerUrl,
 AzureBlobType,
 AzureAccessTier,
 Subdirectory,
 Tags,
 region
)
SELECT 
 '{{ AgentArns }}',
 '{{ AzureBlobAuthenticationType }}',
 '{{ AzureBlobSasConfiguration }}',
 '{{ AzureBlobContainerUrl }}',
 '{{ AzureBlobType }}',
 '{{ AzureAccessTier }}',
 '{{ Subdirectory }}',
 '{{ Tags }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: location_azure_blob
    props:
      - name: AgentArns
        value:
          - '{{ AgentArns[0] }}'
      - name: AzureBlobAuthenticationType
        value: '{{ AzureBlobAuthenticationType }}'
      - name: AzureBlobSasConfiguration
        value:
          AzureBlobSasToken: '{{ AzureBlobSasToken }}'
      - name: AzureBlobContainerUrl
        value: '{{ AzureBlobContainerUrl }}'
      - name: AzureBlobType
        value: '{{ AzureBlobType }}'
      - name: AzureAccessTier
        value: '{{ AzureAccessTier }}'
      - name: Subdirectory
        value: '{{ Subdirectory }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datasync.location_azure_blobs
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>location_azure_blobs</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationAzureBlob,
datasync:DescribeLocationAzureBlob,
datasync:TagResource,
datasync:ListTagsForResource
```

### Read
```json
datasync:DescribeLocationAzureBlob,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationAzureBlob,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
datasync:UpdateLocationAzureBlob
```

### Delete
```json
datasync:DeleteLocation
```

### List
```json
datasync:ListLocations
```

