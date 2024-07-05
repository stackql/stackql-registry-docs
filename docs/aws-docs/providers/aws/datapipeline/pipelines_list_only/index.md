---
title: pipelines_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - pipelines_list_only
  - datapipeline
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

Lists <code>pipelines</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/pipelines/"><code>pipelines</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipelines_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datapipeline.pipelines_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="activate" /></td><td><code>boolean</code></td><td>Indicates whether to validate and start the pipeline or stop an active pipeline. By default, the value is set to true.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the pipeline.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the pipeline.</td></tr>
<tr><td><CopyableCode code="parameter_objects" /></td><td><code>array</code></td><td>The parameter objects used with the pipeline.</td></tr>
<tr><td><CopyableCode code="parameter_values" /></td><td><code>array</code></td><td>The parameter values used with the pipeline.</td></tr>
<tr><td><CopyableCode code="pipeline_objects" /></td><td><code>array</code></td><td>The objects that define the pipeline. These objects overwrite the existing pipeline definition. Not all objects, fields, and values can be updated. For information about restrictions, see Editing Your Pipeline in the AWS Data Pipeline Developer Guide.</td></tr>
<tr><td><CopyableCode code="pipeline_tags" /></td><td><code>array</code></td><td>A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see Controlling Access to Pipelines and Resources in the AWS Data Pipeline Developer Guide.</td></tr>
<tr><td><CopyableCode code="pipeline_id" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>pipelines</code> in a region.
```sql
SELECT
region,
pipeline_id
FROM aws.datapipeline.pipelines_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>pipelines_list_only</code> resource, see <a href="/providers/aws/datapipeline/pipelines/#permissions"><code>pipelines</code></a>


