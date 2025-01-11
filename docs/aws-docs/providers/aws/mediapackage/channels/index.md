---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
  - mediapackage
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

Creates, updates, deletes or gets a <code>channel</code> resource or lists <code>channels</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::Channel</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.channels" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) assigned to the Channel.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Channel.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A short text description of the Channel.</td></tr>
<tr><td><CopyableCode code="hls_ingest" /></td><td><code>object</code></td><td>An HTTP Live Streaming (HLS) ingest resource configuration.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
<tr><td><CopyableCode code="egress_access_logs" /></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
<tr><td><CopyableCode code="ingress_access_logs" /></td><td><code>object</code></td><td>The configuration parameters for egress access logging.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediapackage-channel.html"><code>AWS::MediaPackage::Channel</code></a>.

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
    <td><CopyableCode code="Id, region" /></td>
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
Gets all <code>channels</code> in a region.
```sql
SELECT
region,
arn,
id,
description,
hls_ingest,
tags,
egress_access_logs,
ingress_access_logs
FROM aws.mediapackage.channels
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>channel</code>.
```sql
SELECT
region,
arn,
id,
description,
hls_ingest,
tags,
egress_access_logs,
ingress_access_logs
FROM aws.mediapackage.channels
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channel</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediapackage.channels (
 Id,
 region
)
SELECT 
'{{ Id }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediapackage.channels (
 Id,
 Description,
 HlsIngest,
 Tags,
 EgressAccessLogs,
 IngressAccessLogs,
 region
)
SELECT 
 '{{ Id }}',
 '{{ Description }}',
 '{{ HlsIngest }}',
 '{{ Tags }}',
 '{{ EgressAccessLogs }}',
 '{{ IngressAccessLogs }}',
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
  - name: channel
    props:
      - name: Id
        value: '{{ Id }}'
      - name: Description
        value: '{{ Description }}'
      - name: HlsIngest
        value:
          ingestEndpoints:
            - Id: '{{ Id }}'
              Username: '{{ Username }}'
              Password: '{{ Password }}'
              Url: '{{ Url }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: EgressAccessLogs
        value:
          LogGroupName: '{{ LogGroupName }}'
      - name: IngressAccessLogs
        value: null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.mediapackage.channels
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channels</code> resource, the following permissions are required:

### Create
```json
mediapackage:CreateChannel,
mediapackage:DescribeChannel,
mediapackage:UpdateChannel,
mediapackage:TagResource,
mediapackage:ConfigureLogs,
iam:CreateServiceLinkedRole
```

### Read
```json
mediapackage:DescribeChannel
```

### Update
```json
mediapackage:UpdateChannel,
mediapackage:ConfigureLogs,
iam:CreateServiceLinkedRole
```

### Delete
```json
mediapackage:DeleteChannel
```

### List
```json
mediapackage:ListChannels
```
