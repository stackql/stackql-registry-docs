---
title: view_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - view_versions
  - connect
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

Creates, updates, deletes or gets a <code>view_version</code> resource or lists <code>view_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>view_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::ViewVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.view_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="view_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the view for which a version is being created.</td></tr>
<tr><td><CopyableCode code="view_version_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the created view version.</td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td>The description for the view version.</td></tr>
<tr><td><CopyableCode code="view_content_sha256" /></td><td><code>string</code></td><td>The view content hash to be checked.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>integer</code></td><td>The version of the view.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-viewversion.html"><code>AWS::Connect::ViewVersion</code></a>.

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
    <td><CopyableCode code="ViewArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>view_versions</code> in a region.
```sql
SELECT
region,
view_arn,
view_version_arn,
version_description,
view_content_sha256,
version
FROM aws.connect.view_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>view_version</code>.
```sql
SELECT
region,
view_arn,
view_version_arn,
version_description,
view_content_sha256,
version
FROM aws.connect.view_versions
WHERE region = 'us-east-1' AND data__Identifier = '<ViewVersionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>view_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.view_versions (
 ViewArn,
 region
)
SELECT 
'{{ ViewArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.view_versions (
 ViewArn,
 VersionDescription,
 ViewContentSha256,
 region
)
SELECT 
 '{{ ViewArn }}',
 '{{ VersionDescription }}',
 '{{ ViewContentSha256 }}',
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
  - name: view_version
    props:
      - name: ViewArn
        value: '{{ ViewArn }}'
      - name: VersionDescription
        value: '{{ VersionDescription }}'
      - name: ViewContentSha256
        value: '{{ ViewContentSha256 }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.view_versions
WHERE data__Identifier = '<ViewVersionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>view_versions</code> resource, the following permissions are required:

### Create
```json
connect:CreateViewVersion
```

### Read
```json
connect:DescribeView
```

### List
```json
connect:ListViewVersions
```

### Delete
```json
connect:DeleteViewVersion
```
