---
title: archives
hide_title: false
hide_table_of_contents: false
keywords:
  - archives
  - events
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

Creates, updates, deletes or gets an <code>archive</code> resource or lists <code>archives</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>archives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Events::Archive</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.events.archives" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="archive_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="event_pattern" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="retention_days" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-events-archive.html"><code>AWS::Events::Archive</code></a>.

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
    <td><CopyableCode code="SourceArn, region" /></td>
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
Gets all <code>archives</code> in a region.
```sql
SELECT
region,
archive_name,
source_arn,
description,
event_pattern,
arn,
retention_days
FROM aws.events.archives
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>archive</code>.
```sql
SELECT
region,
archive_name,
source_arn,
description,
event_pattern,
arn,
retention_days
FROM aws.events.archives
WHERE region = 'us-east-1' AND data__Identifier = '<ArchiveName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>archive</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.events.archives (
 SourceArn,
 region
)
SELECT 
'{{ SourceArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.events.archives (
 ArchiveName,
 SourceArn,
 Description,
 EventPattern,
 RetentionDays,
 region
)
SELECT 
 '{{ ArchiveName }}',
 '{{ SourceArn }}',
 '{{ Description }}',
 '{{ EventPattern }}',
 '{{ RetentionDays }}',
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
  - name: archive
    props:
      - name: ArchiveName
        value: '{{ ArchiveName }}'
      - name: SourceArn
        value: '{{ SourceArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: EventPattern
        value: {}
      - name: RetentionDays
        value: '{{ RetentionDays }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.events.archives
WHERE data__Identifier = '<ArchiveName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>archives</code> resource, the following permissions are required:

### Create
```json
events:DescribeArchive,
events:CreateArchive
```

### Delete
```json
events:DescribeArchive,
events:DeleteArchive
```

### List
```json
events:ListArchives
```

### Update
```json
events:DescribeArchive,
events:UpdateArchive
```

### Read
```json
events:DescribeArchive
```
