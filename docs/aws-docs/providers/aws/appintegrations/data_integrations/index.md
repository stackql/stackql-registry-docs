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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>data_integration</code> resource or lists <code>data_integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppIntegrations::DataIntegration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appintegrations.data_integrations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The data integration description.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="Name, KmsKey, SourceURI, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>data_integrations</code> in a region.
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
FROM aws.appintegrations.data_integrations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>data_integration</code>.
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
FROM aws.appintegrations.data_integrations
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_integration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appintegrations.data_integrations (
 Name,
 KmsKey,
 SourceURI,
 region
)
SELECT 
'{{ Name }}',
 '{{ KmsKey }}',
 '{{ SourceURI }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appintegrations.data_integrations (
 Description,
 Name,
 KmsKey,
 ScheduleConfig,
 SourceURI,
 Tags,
 FileConfiguration,
 ObjectConfiguration,
 region
)
SELECT 
 '{{ Description }}',
 '{{ Name }}',
 '{{ KmsKey }}',
 '{{ ScheduleConfig }}',
 '{{ SourceURI }}',
 '{{ Tags }}',
 '{{ FileConfiguration }}',
 '{{ ObjectConfiguration }}',
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
  - name: data_integration
    props:
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: KmsKey
        value: '{{ KmsKey }}'
      - name: ScheduleConfig
        value:
          FirstExecutionFrom: '{{ FirstExecutionFrom }}'
          Object: '{{ Object }}'
          ScheduleExpression: '{{ ScheduleExpression }}'
      - name: SourceURI
        value: '{{ SourceURI }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: FileConfiguration
        value:
          Folders:
            - '{{ Folders[0] }}'
          Filters: {}
      - name: ObjectConfiguration
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appintegrations.data_integrations
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>data_integrations</code> resource, the following permissions are required:

### Create
```json
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
s3:GetEncryptionConfiguration
```

### Read
```json
app-integrations:GetDataIntegration,
app-integrations:ListTagsForResource
```

### List
```json
app-integrations:ListDataIntegrations
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

