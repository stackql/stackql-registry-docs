---
title: resolvers
hide_title: false
hide_table_of_contents: false
keywords:
  - resolvers
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
Retrieves a list of <code>resolvers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolvers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appsync.resolvers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>TypeName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>PipelineConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RequestMappingTemplate</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResponseMappingTemplate</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MaxBatchSize</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ResolverArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SyncConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Code</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ResponseMappingTemplateS3Location</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Runtime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CodeS3Location</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DataSourceName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Kind</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CachingConfig</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>RequestMappingTemplateS3Location</code></td><td><code>string</code></td><td></td></tr><tr><td><code>FieldName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ApiId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.appsync.resolvers
WHERE region = 'us-east-1'
```
