---
title: application_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - application_tags
  - kinesisanalyticsv2
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

Expands all tag keys and values for <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates an Amazon Kinesis Data Analytics application. For information about creating a Kinesis Data Analytics application, see &#91;Creating an Application&#93;(https://docs.aws.amazon.com/kinesisanalytics/latest/java/getting-started.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisanalyticsv2.application_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_configuration" /></td><td><code>object</code></td><td>Use this parameter to configure the application.</td></tr>
<tr><td><CopyableCode code="application_description" /></td><td><code>string</code></td><td>The description of the application.</td></tr>
<tr><td><CopyableCode code="application_mode" /></td><td><code>string</code></td><td>To create a Kinesis Data Analytics Studio notebook, you must set the mode to `INTERACTIVE`. However, for a Kinesis Data Analytics for Apache Flink application, the mode is optional.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application.</td></tr>
<tr><td><CopyableCode code="runtime_environment" /></td><td><code>string</code></td><td>The runtime environment for the application.</td></tr>
<tr><td><CopyableCode code="service_execution_role" /></td><td><code>string</code></td><td>Specifies the IAM role that the application uses to access external resources.</td></tr>
<tr><td><CopyableCode code="run_configuration" /></td><td><code>object</code></td><td>Specifies run configuration (start parameters) of a Kinesis Data Analytics application. Evaluated on update for RUNNING applications an only.</td></tr>
<tr><td><CopyableCode code="application_maintenance_configuration" /></td><td><code>object</code></td><td>Used to configure start of maintenance window.</td></tr>
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
Expands tags for all <code>applications</code> in a region.
```sql
SELECT
region,
application_configuration,
application_description,
application_mode,
application_name,
runtime_environment,
service_execution_role,
run_configuration,
application_maintenance_configuration,
tag_key,
tag_value
FROM aws.kinesisanalyticsv2.application_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_tags</code> resource, see <a href="/providers/aws/kinesisanalyticsv2/applications/#permissions"><code>applications</code></a>

