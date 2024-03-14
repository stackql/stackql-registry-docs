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
Gets an individual <code>application_version</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application_version</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticbeanstalk.application_version</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application that is associated with this application version. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of this application version.</td></tr>
<tr><td><code>source_bundle</code></td><td><code>object</code></td><td>The Amazon S3 bucket and key that identify the location of the source bundle for this version. </td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
application_name,
description,
source_bundle
FROM awscc.elasticbeanstalk.application_version
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

