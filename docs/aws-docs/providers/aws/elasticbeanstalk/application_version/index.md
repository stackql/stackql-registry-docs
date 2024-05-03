---
title: application_version
hide_title: false
hide_table_of_contents: false
keywords:
  - application_version
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

Gets or operates on an individual <code>application_version</code> resource, use <code>application_versions</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::ApplicationVersion</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.application_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application that is associated with this application version. </td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of this application version.</td></tr>
<tr><td><CopyableCode code="source_bundle" /></td><td><code>object</code></td><td>The Amazon S3 bucket and key that identify the location of the source bundle for this version. </td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
id,
application_name,
description,
source_bundle
FROM aws.elasticbeanstalk.application_version
WHERE data__Identifier = '<ApplicationName>|<Id>';
```

## Permissions

To operate on the <code>application_version</code> resource, the following permissions are required:

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

