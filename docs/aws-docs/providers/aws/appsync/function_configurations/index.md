---
title: function_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - function_configurations
  - appsync
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>function_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>function_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.function_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FunctionId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FunctionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RequestMappingTemplate</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResponseMappingTemplate</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MaxBatchSize</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>SyncConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Code</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResponseMappingTemplateS3Location</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Runtime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CodeS3Location</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DataSourceName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FunctionVersion</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RequestMappingTemplateS3Location</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.appsync.function_configurations
WHERE region = 'us-east-1'
```
