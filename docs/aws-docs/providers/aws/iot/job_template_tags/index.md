---
title: job_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - job_template_tags
  - iot
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

Expands all tag keys and values for <code>job_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.job_template_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="job_arn" /></td><td><code>string</code></td><td>Optional for copying a JobTemplate from a pre-existing Job configuration.</td></tr>
<tr><td><CopyableCode code="job_template_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the Job Template.</td></tr>
<tr><td><CopyableCode code="document" /></td><td><code>string</code></td><td>The job document. Required if you don't specify a value for documentSource.</td></tr>
<tr><td><CopyableCode code="document_source" /></td><td><code>string</code></td><td>An S3 link to the job document to use in the template. Required if you don't specify a value for document.</td></tr>
<tr><td><CopyableCode code="timeout_config" /></td><td><code>object</code></td><td>Specifies the amount of time each device has to finish its execution of the job.</td></tr>
<tr><td><CopyableCode code="job_executions_rollout_config" /></td><td><code>object</code></td><td>Allows you to create a staged rollout of a job.</td></tr>
<tr><td><CopyableCode code="abort_config" /></td><td><code>object</code></td><td>The criteria that determine when and how a job abort takes place.</td></tr>
<tr><td><CopyableCode code="presigned_url_config" /></td><td><code>object</code></td><td>Configuration for pre-signed S3 URLs.</td></tr>
<tr><td><CopyableCode code="job_executions_retry_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="maintenance_windows" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="destination_package_versions" /></td><td><code>array</code></td><td></td></tr>
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
Expands tags for all <code>job_templates</code> in a region.
```sql
SELECT
region,
arn,
job_arn,
job_template_id,
description,
document,
document_source,
timeout_config,
job_executions_rollout_config,
abort_config,
presigned_url_config,
job_executions_retry_config,
maintenance_windows,
destination_package_versions,
tag_key,
tag_value
FROM aws.iot.job_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>job_template_tags</code> resource, see <a href="/providers/aws/iot/job_templates/#permissions"><code>job_templates</code></a>

