---
title: environments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_list_only
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>environments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/environments/"><code>environments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MWAA::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mwaa.environments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Customer-defined identifier for the environment, unique per customer region.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>ARN for the MWAA environment.</td></tr>
<tr><td><CopyableCode code="webserver_url" /></td><td><code>string</code></td><td>Url endpoint for the environment's Airflow UI.</td></tr>
<tr><td><CopyableCode code="execution_role_arn" /></td><td><code>string</code></td><td>IAM role to be used by tasks.</td></tr>
<tr><td><CopyableCode code="kms_key" /></td><td><code>string</code></td><td>The identifier of the AWS Key Management Service (AWS KMS) customer master key (CMK) to use for MWAA data encryption.<br />You can specify the CMK using any of the following:<br />Key ID. For example, key/1234abcd-12ab-34cd-56ef-1234567890ab.<br />Key alias. For example, alias/ExampleAlias.<br />Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef.<br />Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.<br />AWS authenticates the CMK asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</td></tr>
<tr><td><CopyableCode code="airflow_version" /></td><td><code>string</code></td><td>Version of airflow to deploy to the environment.</td></tr>
<tr><td><CopyableCode code="source_bucket_arn" /></td><td><code>string</code></td><td>ARN for the AWS S3 bucket to use as the source of DAGs and plugins for the environment.</td></tr>
<tr><td><CopyableCode code="dag_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="plugins_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="plugins_s3_object_version" /></td><td><code>string</code></td><td>Represents an version ID for an S3 object.</td></tr>
<tr><td><CopyableCode code="requirements_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="requirements_s3_object_version" /></td><td><code>string</code></td><td>Represents an version ID for an S3 object.</td></tr>
<tr><td><CopyableCode code="startup_script_s3_path" /></td><td><code>string</code></td><td>Represents an S3 prefix relative to the root of an S3 bucket.</td></tr>
<tr><td><CopyableCode code="startup_script_s3_object_version" /></td><td><code>string</code></td><td>Represents an version ID for an S3 object.</td></tr>
<tr><td><CopyableCode code="airflow_configuration_options" /></td><td><code>object</code></td><td>Key/value pairs representing Airflow configuration variables.<br />Keys are prefixed by their section:<br />&#91;core&#93;<br />dags_folder=&#123;AIRFLOW_HOME&#125;/dags<br />Would be represented as<br />"core.dags_folder": "&#123;AIRFLOW_HOME&#125;/dags"</td></tr>
<tr><td><CopyableCode code="environment_class" /></td><td><code>string</code></td><td>Templated configuration for airflow processes and backing infrastructure.</td></tr>
<tr><td><CopyableCode code="max_workers" /></td><td><code>integer</code></td><td>Maximum worker compute units.</td></tr>
<tr><td><CopyableCode code="min_workers" /></td><td><code>integer</code></td><td>Minimum worker compute units.</td></tr>
<tr><td><CopyableCode code="max_webservers" /></td><td><code>integer</code></td><td>Maximum webserver compute units.</td></tr>
<tr><td><CopyableCode code="min_webservers" /></td><td><code>integer</code></td><td>Minimum webserver compute units.</td></tr>
<tr><td><CopyableCode code="schedulers" /></td><td><code>integer</code></td><td>Scheduler compute units.</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>Configures the network resources of the environment.</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td>Logging configuration for the environment.</td></tr>
<tr><td><CopyableCode code="weekly_maintenance_window_start" /></td><td><code>string</code></td><td>Start time for the weekly maintenance window.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A map of tags for the environment.</td></tr>
<tr><td><CopyableCode code="webserver_access_mode" /></td><td><code>string</code></td><td>Choice for mode of webserver access including over public internet or via private VPC endpoint.</td></tr>
<tr><td><CopyableCode code="endpoint_management" /></td><td><code>string</code></td><td>Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA.</td></tr>
<tr><td><CopyableCode code="celery_executor_queue" /></td><td><code>string</code></td><td>The celery executor queue associated with the environment.</td></tr>
<tr><td><CopyableCode code="database_vpc_endpoint_service" /></td><td><code>string</code></td><td>The database VPC endpoint service name.</td></tr>
<tr><td><CopyableCode code="webserver_vpc_endpoint_service" /></td><td><code>string</code></td><td>The webserver VPC endpoint service name, applicable if private webserver access mode selected.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>environments</code> in a region.
```sql
SELECT
region,
name
FROM aws.mwaa.environments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environments_list_only</code> resource, see <a href="/providers/aws/mwaa/environments/#permissions"><code>environments</code></a>


