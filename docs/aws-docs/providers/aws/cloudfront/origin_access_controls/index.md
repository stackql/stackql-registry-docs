---
title: origin_access_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - origin_access_controls
  - cloudfront
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

Creates, updates, deletes or gets an <code>origin_access_control</code> resource or lists <code>origin_access_controls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>origin_access_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::CloudFront::OriginAccessControl</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudfront.origin_access_controls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="origin_access_control_config" /></td><td><code>undefined</code></td><td></td></tr>
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
    <td><CopyableCode code="OriginAccessControlConfig, region" /></td>
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
List all <code>origin_access_controls</code> in a region.
```sql
SELECT
region,
id
FROM aws.cloudfront.origin_access_controls
;
```
Gets all properties from an <code>origin_access_control</code>.
```sql
SELECT
region,
id,
origin_access_control_config
FROM aws.cloudfront.origin_access_controls
WHERE data__Identifier = '<Id>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>origin_access_control</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cloudfront.origin_access_controls (
 OriginAccessControlConfig,
 region
)
SELECT 
'{{ OriginAccessControlConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cloudfront.origin_access_controls (
 OriginAccessControlConfig,
 region
)
SELECT 
 '{{ OriginAccessControlConfig }}',
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
  - name: origin_access_control
    props:
      - name: OriginAccessControlConfig
        value:
          Description: '{{ Description }}'
          Name: '{{ Name }}'
          OriginAccessControlOriginType: '{{ OriginAccessControlOriginType }}'
          SigningBehavior: '{{ SigningBehavior }}'
          SigningProtocol: '{{ SigningProtocol }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cloudfront.origin_access_controls
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>origin_access_controls</code> resource, the following permissions are required:

### Create
```json
cloudfront:CreateOriginAccessControl
```

### Delete
```json
cloudfront:DeleteOriginAccessControl,
cloudfront:GetOriginAccessControl
```

### List
```json
cloudfront:ListOriginAccessControls
```

### Read
```json
cloudfront:GetOriginAccessControl
```

### Update
```json
cloudfront:UpdateOriginAccessControl,
cloudfront:GetOriginAccessControl
```

