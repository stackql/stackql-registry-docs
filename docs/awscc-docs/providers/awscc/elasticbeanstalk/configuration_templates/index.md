---
title: configuration_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_templates
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
Retrieves a list of <code>configuration_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_templates</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticbeanstalk.configuration_templates</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application to associate with this configuration template. </td></tr>
<tr><td><code>template_name</code></td><td><code>string</code></td><td>The name of the configuration template</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>configuration_templates</code> resource, the following permissions are required:

### Create
```json
elasticbeanstalk:CreateConfigurationTemplate
```

### List
```json
elasticbeanstalk:DescribeApplications
```


## Example
```sql
SELECT
region,
application_name,
template_name
FROM awscc.elasticbeanstalk.configuration_templates
WHERE region = 'us-east-1'
```
