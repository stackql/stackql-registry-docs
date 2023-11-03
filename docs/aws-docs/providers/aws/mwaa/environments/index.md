---
title: environments
hide_title: false
hide_table_of_contents: false
keywords:
  - environments
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
Retrieves a list of <code>environments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.mwaa.environments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Name</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>WebserverUrl</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>ExecutionRoleArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>KmsKey</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AirflowVersion</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>SourceBucketArn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>DagS3Path</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PluginsS3Path</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>PluginsS3ObjectVersion</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RequirementsS3Path</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RequirementsS3ObjectVersion</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StartupScriptS3Path</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StartupScriptS3ObjectVersion</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AirflowConfigurationOptions</code></td><td><code>object</code></td><td>Key/value pairs representing Airflow configuration variables.
    Keys are prefixed by their section:

    [core]
    dags_folder={AIRFLOW_HOME}/dags

    Would be represented as

    "core.dags_folder": "{AIRFLOW_HOME}/dags"</td></tr><tr><td><code>EnvironmentClass</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>MaxWorkers</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>MinWorkers</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Schedulers</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>NetworkConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>LoggingConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>WeeklyMaintenanceWindowStart</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>object</code></td><td>A map of tags for the environment.</td></tr><tr><td><code>WebserverAccessMode</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.mwaa.environments
WHERE region = 'us-east-1'
```
