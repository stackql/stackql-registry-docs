---
title: live_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - live_sources
  - mediatailor
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

Creates, updates, deletes or gets a <code>live_source</code> resource or lists <code>live_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::MediaTailor::LiveSource Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediatailor.live_sources" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td><p>The ARN of the live source.</p></td></tr>
<tr><td><CopyableCode code="http_package_configurations" /></td><td><code>array</code></td><td><p>A list of HTTP package configuration parameters for this live source.</p></td></tr>
<tr><td><CopyableCode code="live_source_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_location_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to assign to the live source.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediatailor-livesource.html"><code>AWS::MediaTailor::LiveSource</code></a>.

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
    <td><CopyableCode code="HttpPackageConfigurations, LiveSourceName, SourceLocationName, region" /></td>
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
Gets all <code>live_sources</code> in a region.
```sql
SELECT
region,
arn,
http_package_configurations,
live_source_name,
source_location_name,
tags
FROM aws.mediatailor.live_sources
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>live_source</code>.
```sql
SELECT
region,
arn,
http_package_configurations,
live_source_name,
source_location_name,
tags
FROM aws.mediatailor.live_sources
WHERE region = 'us-east-1' AND data__Identifier = '<LiveSourceName>|<SourceLocationName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>live_source</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediatailor.live_sources (
 HttpPackageConfigurations,
 LiveSourceName,
 SourceLocationName,
 region
)
SELECT 
'{{ HttpPackageConfigurations }}',
 '{{ LiveSourceName }}',
 '{{ SourceLocationName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediatailor.live_sources (
 HttpPackageConfigurations,
 LiveSourceName,
 SourceLocationName,
 Tags,
 region
)
SELECT 
 '{{ HttpPackageConfigurations }}',
 '{{ LiveSourceName }}',
 '{{ SourceLocationName }}',
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
  - name: live_source
    props:
      - name: HttpPackageConfigurations
        value:
          - Path: '{{ Path }}'
            SourceGroup: '{{ SourceGroup }}'
            Type: '{{ Type }}'
      - name: LiveSourceName
        value: '{{ LiveSourceName }}'
      - name: SourceLocationName
        value: '{{ SourceLocationName }}'
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
DELETE FROM aws.mediatailor.live_sources
WHERE data__Identifier = '<LiveSourceName|SourceLocationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>live_sources</code> resource, the following permissions are required:

### Create
```json
mediatailor:CreateLiveSource,
mediatailor:DescribeLiveSource,
mediatailor:TagResource
```

### Read
```json
mediatailor:DescribeLiveSource
```

### Update
```json
mediatailor:UpdateLiveSource,
mediatailor:DescribeLiveSource,
mediatailor:TagResource,
mediatailor:UntagResource
```

### Delete
```json
mediatailor:DeleteLiveSource,
mediatailor:DescribeLiveSource
```

### List
```json
mediatailor:ListLiveSources
```
