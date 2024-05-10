---
title: links
hide_title: false
hide_table_of_contents: false
keywords:
  - links
  - oam
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


Used to retrieve a list of <code>links</code> in a region or to create or delete a <code>links</code> resource, use <code>link</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Oam::Link Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.oam.links" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn
FROM aws.oam.links
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>link</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
-- link.iql (required properties only)
INSERT INTO aws.oam.links (
 ResourceTypes,
 SinkIdentifier,
 region
)
SELECT 
'{{ ResourceTypes }}',
 '{{ SinkIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- link.iql (all properties)
INSERT INTO aws.oam.links (
 LabelTemplate,
 ResourceTypes,
 SinkIdentifier,
 LinkConfiguration,
 Tags,
 region
)
SELECT 
 '{{ LabelTemplate }}',
 '{{ ResourceTypes }}',
 '{{ SinkIdentifier }}',
 '{{ LinkConfiguration }}',
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
  - name: link
    props:
      - name: LabelTemplate
        value: '{{ LabelTemplate }}'
      - name: ResourceTypes
        value:
          - '{{ ResourceTypes[0] }}'
      - name: SinkIdentifier
        value: '{{ SinkIdentifier }}'
      - name: LinkConfiguration
        value:
          MetricConfiguration:
            Filter: '{{ Filter }}'
          LogGroupConfiguration: null
      - name: Tags
        value: {}

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.oam.links
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>links</code> resource, the following permissions are required:

### Create
```json
oam:CreateLink,
oam:GetLink,
cloudwatch:Link,
logs:Link,
xray:Link,
applicationinsights:Link,
internetmonitor:Link
```

### Delete
```json
oam:DeleteLink,
oam:GetLink
```

### List
```json
oam:ListLinks
```

