---
title: usage_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - usage_profiles
  - glue
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

Creates, updates, deletes or gets an <code>usage_profile</code> resource or lists <code>usage_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>usage_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This creates a Resource of UsageProfile type.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.usage_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the UsageProfile.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the UsageProfile.</td></tr>
<tr><td><CopyableCode code="configuration" /></td><td><code>undefined</code></td><td>UsageProfile configuration for supported service ex: (Jobs, Sessions).</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to be applied to this UsageProfiles.</td></tr>
<tr><td><CopyableCode code="created_on" /></td><td><code>string</code></td><td>Creation time.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-glue-usageprofile.html"><code>AWS::Glue::UsageProfile</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>usage_profiles</code> in a region.
```sql
SELECT
region,
name,
description,
configuration,
tags,
created_on
FROM aws.glue.usage_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>usage_profile</code>.
```sql
SELECT
region,
name,
description,
configuration,
tags,
created_on
FROM aws.glue.usage_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>usage_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.glue.usage_profiles (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.glue.usage_profiles (
 Name,
 Description,
 Configuration,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ Configuration }}',
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
  - name: usage_profile
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: Configuration
        value: null
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
DELETE FROM aws.glue.usage_profiles
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>usage_profiles</code> resource, the following permissions are required:

### Create
```json
glue:CreateUsageProfile,
glue:GetUsageProfile,
glue:GetTags,
glue:TagResource
```

### Read
```json
glue:GetUsageProfile,
glue:GetTags
```

### Update
```json
glue:UpdateUsageProfile,
glue:GetUsageProfile,
glue:TagResource,
glue:UntagResource,
glue:GetTags
```

### Delete
```json
glue:DeleteUsageProfile,
glue:GetUsageProfile
```

### List
```json
glue:ListUsageProfiles
```
