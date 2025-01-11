---
title: mlflow_tracking_server_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - mlflow_tracking_server_tags
  - sagemaker
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

Expands all tag keys and values for <code>mlflow_tracking_servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mlflow_tracking_server_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SageMaker::MlflowTrackingServer</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sagemaker.mlflow_tracking_server_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="tracking_server_name" /></td><td><code>string</code></td><td>The name of the MLFlow Tracking Server.</td></tr>
<tr><td><CopyableCode code="tracking_server_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the MLFlow Tracking Server.</td></tr>
<tr><td><CopyableCode code="tracking_server_size" /></td><td><code>string</code></td><td>The size of the MLFlow Tracking Server.</td></tr>
<tr><td><CopyableCode code="mlflow_version" /></td><td><code>string</code></td><td>The MLFlow Version used on the MLFlow Tracking Server.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker to perform tasks on behalf of the customer.</td></tr>
<tr><td><CopyableCode code="artifact_store_uri" /></td><td><code>string</code></td><td>The Amazon S3 URI for MLFlow Tracking Server artifacts.</td></tr>
<tr><td><CopyableCode code="automatic_model_registration" /></td><td><code>boolean</code></td><td>A flag to enable Automatic SageMaker Model Registration.</td></tr>
<tr><td><CopyableCode code="weekly_maintenance_window_start" /></td><td><code>string</code></td><td>The start of the time window for maintenance of the MLFlow Tracking Server in UTC time.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>mlflow_tracking_servers</code> in a region.
```sql
SELECT
region,
tracking_server_name,
tracking_server_arn,
tracking_server_size,
mlflow_version,
role_arn,
artifact_store_uri,
automatic_model_registration,
weekly_maintenance_window_start,
tag_key,
tag_value
FROM aws.sagemaker.mlflow_tracking_server_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>mlflow_tracking_server_tags</code> resource, see <a href="/providers/aws/sagemaker/mlflow_tracking_servers/#permissions"><code>mlflow_tracking_servers</code></a>

