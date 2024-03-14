---
title: resolver
hide_title: false
hide_table_of_contents: false
keywords:
  - resolver
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
Gets an individual <code>resolver</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolver</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>resolver</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appsync.resolver</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>api_id</code></td><td><code>string</code></td><td>The APSYlong GraphQL API to which you want to attach this resolver.</td></tr>
<tr><td><code>caching_config</code></td><td><code>object</code></td><td>The caching configuration for the resolver.</td></tr>
<tr><td><code>code</code></td><td><code>string</code></td><td>The ``resolver`` code that contains the request and response functions. When code is used, the ``runtime`` is required. The runtime value must be ``APPSYNC_JS``.</td></tr>
<tr><td><code>code_s3_location</code></td><td><code>string</code></td><td>The Amazon S3 endpoint.</td></tr>
<tr><td><code>data_source_name</code></td><td><code>string</code></td><td>The resolver data source name.</td></tr>
<tr><td><code>field_name</code></td><td><code>string</code></td><td>The GraphQL field on a type that invokes the resolver.</td></tr>
<tr><td><code>kind</code></td><td><code>string</code></td><td>The resolver type.&lt;br&#x2F;&gt;  +   *UNIT*: A UNIT resolver type. A UNIT resolver is the default resolver type. You can use a UNIT resolver to run a GraphQL query against a single data source.&lt;br&#x2F;&gt;  +   *PIPELINE*: A PIPELINE resolver type. You can use a PIPELINE resolver to invoke a series of ``Function`` objects in a serial manner. You can use a pipeline resolver to run a GraphQL query against multiple data sources.</td></tr>
<tr><td><code>max_batch_size</code></td><td><code>integer</code></td><td>The maximum number of resolver request inputs that will be sent to a single LAMlong function in a ``BatchInvoke`` operation.</td></tr>
<tr><td><code>pipeline_config</code></td><td><code>object</code></td><td>Functions linked with the pipeline resolver.</td></tr>
<tr><td><code>request_mapping_template</code></td><td><code>string</code></td><td>The request mapping template.&lt;br&#x2F;&gt; Request mapping templates are optional when using a Lambda data source. For all other data sources, a request mapping template is required.</td></tr>
<tr><td><code>request_mapping_template_s3_location</code></td><td><code>string</code></td><td>The location of a request mapping template in an S3 bucket. Use this if you want to provision with a template file in S3 rather than embedding it in your CFNshort template.</td></tr>
<tr><td><code>resolver_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>response_mapping_template</code></td><td><code>string</code></td><td>The response mapping template.</td></tr>
<tr><td><code>response_mapping_template_s3_location</code></td><td><code>string</code></td><td>The location of a response mapping template in an S3 bucket. Use this if you want to provision with a template file in S3 rather than embedding it in your CFNshort template.</td></tr>
<tr><td><code>runtime</code></td><td><code>object</code></td><td>Describes a runtime used by an APSYlong resolver or APSYlong function. Specifies the name and version of the runtime to use. Note that if a runtime is specified, code must also be specified.</td></tr>
<tr><td><code>sync_config</code></td><td><code>object</code></td><td>The ``SyncConfig`` for a resolver attached to a versioned data source.</td></tr>
<tr><td><code>type_name</code></td><td><code>string</code></td><td>The GraphQL type that invokes this resolver.</td></tr>
<tr><td><code>metrics_config</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
api_id,
caching_config,
code,
code_s3_location,
data_source_name,
field_name,
kind,
max_batch_size,
pipeline_config,
request_mapping_template,
request_mapping_template_s3_location,
resolver_arn,
response_mapping_template,
response_mapping_template_s3_location,
runtime,
sync_config,
type_name,
metrics_config
FROM awscc.appsync.resolver
WHERE data__Identifier = '<ResolverArn>';
```

## Permissions

To operate on the <code>resolver</code> resource, the following permissions are required:

### Read
```json
appsync:GetResolver
```

### Update
```json
s3:GetObject,
appsync:UpdateResolver
```

### Delete
```json
appsync:DeleteResolver
```

