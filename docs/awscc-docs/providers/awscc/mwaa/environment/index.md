---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
  - mwaa
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mwaa.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>webserver_url</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>execution_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kms_key</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>airflow_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>source_bucket_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>dag_s3_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>plugins_s3_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>plugins_s3_object_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>requirements_s3_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>requirements_s3_object_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>startup_script_s3_path</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>startup_script_s3_object_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>airflow_configuration_options</code></td><td><code>object</code></td><td>Key&#x2F;value pairs representing Airflow configuration variables.&lt;br&#x2F;&gt;    Keys are prefixed by their section:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;    &#91;core&#93;&lt;br&#x2F;&gt;    dags_folder=&#123;AIRFLOW_HOME&#125;&#x2F;dags&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;    Would be represented as&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;    "core.dags_folder": "&#123;AIRFLOW_HOME&#125;&#x2F;dags"</td></tr>
<tr><td><code>environment_class</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_workers</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>min_workers</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>schedulers</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>network_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>logging_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>weekly_maintenance_window_start</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td>A map of tags for the environment.</td></tr>
<tr><td><code>webserver_access_mode</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>endpoint_management</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>celery_executor_queue</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>database_vpc_endpoint_service</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>webserver_vpc_endpoint_service</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
<pre>
airflow:GetEnvironment</pre>

### Update
<pre>
airflow:UpdateEnvironment,
airflow:TagResource,
airflow:UntagResource</pre>

### Delete
<pre>
airflow:DeleteEnvironment</pre>


## Example
```sql
SELECT
region,
name,
arn,
webserver_url,
execution_role_arn,
kms_key,
airflow_version,
source_bucket_arn,
dag_s3_path,
plugins_s3_path,
plugins_s3_object_version,
requirements_s3_path,
requirements_s3_object_version,
startup_script_s3_path,
startup_script_s3_object_version,
airflow_configuration_options,
environment_class,
max_workers,
min_workers,
schedulers,
network_configuration,
logging_configuration,
weekly_maintenance_window_start,
tags,
webserver_access_mode,
endpoint_management,
celery_executor_queue,
database_vpc_endpoint_service,
webserver_vpc_endpoint_service
FROM awscc.mwaa.environment
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Name&gt;'
```
