---
title: experiment_template_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - experiment_template_tags
  - fis
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

Expands all tag keys and values for <code>experiment_templates</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_template_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::FIS::ExperimentTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.fis.experiment_template_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the experiment template.</td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>object</code></td><td>The targets for the experiment.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>object</code></td><td>The actions for the experiment.</td></tr>
<tr><td><CopyableCode code="stop_conditions" /></td><td><code>array</code></td><td>One or more stop conditions.</td></tr>
<tr><td><CopyableCode code="log_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an IAM role that grants the AWS FIS service permission to perform service actions on your behalf.</td></tr>
<tr><td><CopyableCode code="experiment_options" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>experiment_templates</code> in a region.
```sql
SELECT
region,
id,
description,
targets,
actions,
stop_conditions,
log_configuration,
role_arn,
experiment_options,
tag_key,
tag_value
FROM aws.fis.experiment_template_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>experiment_template_tags</code> resource, see <a href="/providers/aws/fis/experiment_templates/#permissions"><code>experiment_templates</code></a>


