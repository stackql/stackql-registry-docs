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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Gets or operates on an individual <code>environment</code> resource, use <code>environments</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MWAA::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mwaa.environment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="webserver_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="airflow_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="source_bucket_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="dag_s3_path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="plugins_s3_path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="plugins_s3_object_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="requirements_s3_path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="requirements_s3_object_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="startup_script_s3_path" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="startup_script_s3_object_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="airflow_configuration_options" /></td><td><code>object</code></td><td>Key&#x2F;value pairs representing Airflow configuration variables.&lt;br&#x2F;&gt;    Keys are prefixed by their section:&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;    &#91;core&#93;&lt;br&#x2F;&gt;    dags_folder=&#123;AIRFLOW_HOME&#125;&#x2F;dags&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;    Would be represented as&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;    "core.dags_folder": "&#123;AIRFLOW_HOME&#125;&#x2F;dags"</td></tr>
<tr><td><CopyableCode code="environment_class" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="max_workers" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="min_workers" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="schedulers" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="weekly_maintenance_window_start" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tags for the environment.</td></tr>
<tr><td><CopyableCode code="webserver_access_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_management" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="celery_executor_queue" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="database_vpc_endpoint_service" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="webserver_vpc_endpoint_service" /></td><td><code>string</code></td><td></td></tr>
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
FROM aws.mwaa.environment
WHERE data__Identifier = '<Name>';
```

## Permissions

To operate on the <code>environment</code> resource, the following permissions are required:

### Read
```json
airflow:GetEnvironment
```

### Update
```json
airflow:UpdateEnvironment,
airflow:TagResource,
airflow:UntagResource
```

### Delete
```json
airflow:DeleteEnvironment
```

