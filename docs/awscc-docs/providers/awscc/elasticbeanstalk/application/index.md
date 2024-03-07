---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
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
Gets an individual <code>application</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>application</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticbeanstalk.application</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td>A name for the Elastic Beanstalk application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Your description of the application.</td></tr>
<tr><td><code>resource_lifecycle_config</code></td><td><code>object</code></td><td>Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>application</code> resource, the following permissions are required:

### Read
<pre>
elasticbeanstalk:DescribeApplications</pre>

### Update
<pre>
elasticbeanstalk:UpdateApplication,
elasticbeanstalk:UpdateApplicationResourceLifecycle</pre>

### Delete
<pre>
elasticbeanstalk:DeleteApplication</pre>


## Example
```sql
SELECT
region,
application_name,
description,
resource_lifecycle_config
FROM awscc.elasticbeanstalk.application
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApplicationName&gt;'
```
