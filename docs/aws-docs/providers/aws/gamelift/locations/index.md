---
title: locations
hide_title: false
hide_table_of_contents: false
keywords:
  - locations
  - gamelift
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

Creates, updates, deletes or gets a <code>location</code> resource or lists <code>locations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Location resource creates an Amazon GameLift (GameLift) custom location.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.locations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="location_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html"><code>AWS::GameLift::Location</code></a>.

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
    <td><CopyableCode code="LocationName, region" /></td>
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
Gets all <code>locations</code> in a region.
```sql
SELECT
region,
location_name,
location_arn,
tags
FROM aws.gamelift.locations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>location</code>.
```sql
SELECT
region,
location_name,
location_arn,
tags
FROM aws.gamelift.locations
WHERE region = 'us-east-1' AND data__Identifier = '<LocationName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>location</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.gamelift.locations (
 LocationName,
 region
)
SELECT 
'{{ LocationName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.locations (
 LocationName,
 Tags,
 region
)
SELECT 
 '{{ LocationName }}',
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
  - name: location
    props:
      - name: LocationName
        value: '{{ LocationName }}'
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
DELETE FROM aws.gamelift.locations
WHERE data__Identifier = '<LocationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>locations</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateLocation,
gamelift:ListLocations,
gamelift:ListTagsForResource,
gamelift:TagResource
```

### Read
```json
gamelift:ListLocations,
gamelift:ListTagsForResource
```

### Delete
```json
gamelift:DeleteLocation
```

### List
```json
gamelift:ListLocations
```

### Update
```json
gamelift:ListLocations,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource
```
