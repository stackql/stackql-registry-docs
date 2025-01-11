---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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

Creates, updates, deletes or gets an <code>application</code> resource or lists <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::ElasticBeanstalk::Application resource specifies an Elastic Beanstalk application.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.applications" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>A name for the Elastic Beanstalk application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Your description of the application.</td></tr>
<tr><td><CopyableCode code="resource_lifecycle_config" /></td><td><code>object</code></td><td>Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticbeanstalk-application.html"><code>AWS::ElasticBeanstalk::Application</code></a>.

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
    <td><CopyableCode code="region" /></td>
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
Gets all <code>applications</code> in a region.
```sql
SELECT
region,
application_name,
description,
resource_lifecycle_config
FROM aws.elasticbeanstalk.applications
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>application</code>.
```sql
SELECT
region,
application_name,
description,
resource_lifecycle_config
FROM aws.elasticbeanstalk.applications
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>application</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticbeanstalk.applications (
 ApplicationName,
 Description,
 ResourceLifecycleConfig,
 region
)
SELECT 
'{{ ApplicationName }}',
 '{{ Description }}',
 '{{ ResourceLifecycleConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticbeanstalk.applications (
 ApplicationName,
 Description,
 ResourceLifecycleConfig,
 region
)
SELECT 
 '{{ ApplicationName }}',
 '{{ Description }}',
 '{{ ResourceLifecycleConfig }}',
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
  - name: application
    props:
      - name: ApplicationName
        value: '{{ ApplicationName }}'
      - name: Description
        value: '{{ Description }}'
      - name: ResourceLifecycleConfig
        value:
          ServiceRole: '{{ ServiceRole }}'
          VersionLifecycleConfig:
            MaxAgeRule:
              DeleteSourceFromS3: '{{ DeleteSourceFromS3 }}'
              Enabled: '{{ Enabled }}'
              MaxAgeInDays: '{{ MaxAgeInDays }}'
            MaxCountRule:
              DeleteSourceFromS3: '{{ DeleteSourceFromS3 }}'
              Enabled: '{{ Enabled }}'
              MaxCount: '{{ MaxCount }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticbeanstalk.applications
WHERE data__Identifier = '<ApplicationName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
```json
elasticbeanstalk:CreateApplication
```

### Read
```json
elasticbeanstalk:DescribeApplications
```

### Update
```json
elasticbeanstalk:UpdateApplication,
elasticbeanstalk:UpdateApplicationResourceLifecycle
```

### Delete
```json
elasticbeanstalk:DeleteApplication
```

### List
```json
elasticbeanstalk:DescribeApplications
```
