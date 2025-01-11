---
title: ingest_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - ingest_configurations
  - ivs
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

Creates, updates, deletes or gets an <code>ingest_configuration</code> resource or lists <code>ingest_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ingest_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::IVS::IngestConfiguration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ivs.ingest_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>IngestConfiguration ARN is automatically generated on creation and assigned as the unique identifier.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>IngestConfiguration</td></tr>
<tr><td><CopyableCode code="stage_arn" /></td><td><code>string</code></td><td>Stage ARN. A value other than an empty string indicates that stage is linked to IngestConfiguration. Default: "" (recording is disabled).</td></tr>
<tr><td><CopyableCode code="participant_id" /></td><td><code>string</code></td><td>Participant Id is automatically generated on creation and assigned.</td></tr>
<tr><td><CopyableCode code="ingest_protocol" /></td><td><code>string</code></td><td>Ingest Protocol.</td></tr>
<tr><td><CopyableCode code="insecure_ingest" /></td><td><code>boolean</code></td><td>Whether ingest configuration allows insecure ingest.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>State of IngestConfiguration which determines whether IngestConfiguration is in use or not.</td></tr>
<tr><td><CopyableCode code="stream_key" /></td><td><code>string</code></td><td>Stream-key value.</td></tr>
<tr><td><CopyableCode code="user_id" /></td><td><code>string</code></td><td>User defined indentifier for participant associated with IngestConfiguration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A list of key-value pairs that contain metadata for the asset model.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ivs-ingestconfiguration.html"><code>AWS::IVS::IngestConfiguration</code></a>.

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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>ingest_configurations</code> in a region.
```sql
SELECT
region,
arn,
name,
stage_arn,
participant_id,
ingest_protocol,
insecure_ingest,
state,
stream_key,
user_id,
tags
FROM aws.ivs.ingest_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>ingest_configuration</code>.
```sql
SELECT
region,
arn,
name,
stage_arn,
participant_id,
ingest_protocol,
insecure_ingest,
state,
stream_key,
user_id,
tags
FROM aws.ivs.ingest_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ingest_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ivs.ingest_configurations (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ivs.ingest_configurations (
 Name,
 StageArn,
 IngestProtocol,
 InsecureIngest,
 UserId,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ StageArn }}',
 '{{ IngestProtocol }}',
 '{{ InsecureIngest }}',
 '{{ UserId }}',
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
  - name: ingest_configuration
    props:
      - name: Name
        value: '{{ Name }}'
      - name: StageArn
        value: '{{ StageArn }}'
      - name: IngestProtocol
        value: '{{ IngestProtocol }}'
      - name: InsecureIngest
        value: '{{ InsecureIngest }}'
      - name: UserId
        value: '{{ UserId }}'
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
DELETE FROM aws.ivs.ingest_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>ingest_configurations</code> resource, the following permissions are required:

### Create
```json
ivs:CreateIngestConfiguration,
ivs:TagResource
```

### Read
```json
ivs:GetIngestConfiguration,
ivs:ListTagsForResource
```

### Update
```json
ivs:GetIngestConfiguration,
ivs:UpdateIngestConfiguration,
ivs:TagResource,
ivs:UntagResource,
ivs:ListTagsForResource
```

### Delete
```json
ivs:DeleteIngestConfiguration,
ivs:UntagResource
```

### List
```json
ivs:ListIngestConfigurations,
ivs:ListTagsForResource
```
