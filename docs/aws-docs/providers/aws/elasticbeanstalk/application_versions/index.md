---
title: application_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_versions
  - elasticbeanstalk
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

Creates, updates, deletes or gets an <code>application_version</code> resource or lists <code>application_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::ApplicationVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.application_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application that is associated with this application version.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of this application version.</td></tr>
<tr><td><CopyableCode code="source_bundle" /></td><td><code>object</code></td><td>The Amazon S3 bucket and key that identify the location of the source bundle for this version.</td></tr>
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
    <td><CopyableCode code="ApplicationName, SourceBundle, region" /></td>
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
Gets all <code>application_versions</code> in a region.
```sql
SELECT
region,
id,
application_name,
description,
source_bundle
FROM aws.elasticbeanstalk.application_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application_version</code>.
```sql
SELECT
region,
id,
application_name,
description,
source_bundle
FROM aws.elasticbeanstalk.application_versions
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationName>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticbeanstalk.application_versions (
 ApplicationName,
 SourceBundle,
 region
)
SELECT 
'{{ ApplicationName }}',
 '{{ SourceBundle }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticbeanstalk.application_versions (
 ApplicationName,
 Description,
 SourceBundle,
 region
)
SELECT 
 '{{ ApplicationName }}',
 '{{ Description }}',
 '{{ SourceBundle }}',
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
  - name: application_version
    props:
      - name: ApplicationName
        value: '{{ ApplicationName }}'
      - name: Description
        value: '{{ Description }}'
      - name: SourceBundle
        value:
          S3Bucket: '{{ S3Bucket }}'
          S3Key: '{{ S3Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticbeanstalk.application_versions
WHERE data__Identifier = '<ApplicationName|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>application_versions</code> resource, the following permissions are required:

### Create
```json
elasticbeanstalk:CreateApplicationVersion,
elasticbeanstalk:DescribeApplicationVersions,
s3:GetObject,
s3:PutObject
```

### Read
```json
elasticbeanstalk:DescribeApplicationVersions
```

### Update
```json
elasticbeanstalk:UpdateApplicationVersion
```

### Delete
```json
elasticbeanstalk:DeleteApplicationVersion
```

### List
```json
elasticbeanstalk:DescribeApplicationVersions
```

