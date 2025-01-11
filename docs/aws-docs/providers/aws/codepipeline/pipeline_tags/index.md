---
title: pipeline_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - pipeline_tags
  - codepipeline
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

Expands all tag keys and values for <code>pipelines</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CodePipeline::Pipeline resource creates a CodePipeline pipeline that describes how software changes go through a release process.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codepipeline.pipeline_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="artifact_stores" /></td><td><code>array</code></td><td>A mapping of artifactStore objects and their corresponding AWS Regions. There must be an artifact store for the pipeline Region and for each cross-region action in the pipeline.</td></tr>
<tr><td><CopyableCode code="disable_inbound_stage_transitions" /></td><td><code>array</code></td><td>Represents the input of a DisableStageTransition action.</td></tr>
<tr><td><CopyableCode code="stages" /></td><td><code>array</code></td><td>Represents information about a stage and its definition.</td></tr>
<tr><td><CopyableCode code="execution_mode" /></td><td><code>string</code></td><td>The method that the pipeline will use to handle multiple executions. The default mode is SUPERSEDED.</td></tr>
<tr><td><CopyableCode code="restart_execution_on_update" /></td><td><code>boolean</code></td><td>Indicates whether to rerun the CodePipeline pipeline after you update it.</td></tr>
<tr><td><CopyableCode code="triggers" /></td><td><code>array</code></td><td>The trigger configuration specifying a type of event, such as Git tags, that starts the pipeline.</td></tr>
<tr><td><CopyableCode code="role_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for CodePipeline to use to either perform actions with no actionRoleArn, or to use to assume roles for actions with an actionRoleArn</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the pipeline.</td></tr>
<tr><td><CopyableCode code="variables" /></td><td><code>array</code></td><td>A list that defines the pipeline variables for a pipeline resource. Variable names can have alphanumeric and underscore characters, and the values must match &#91;A-Za-z0-9@\-_&#93;+.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version of the pipeline.</td></tr>
<tr><td><CopyableCode code="artifact_store" /></td><td><code>object</code></td><td>The S3 bucket where artifacts for the pipeline are stored.</td></tr>
<tr><td><CopyableCode code="pipeline_type" /></td><td><code>string</code></td><td>CodePipeline provides the following pipeline types, which differ in characteristics and price, so that you can tailor your pipeline features and cost to the needs of your applications.</td></tr>
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
Expands tags for all <code>pipelines</code> in a region.
```sql
SELECT
region,
artifact_stores,
disable_inbound_stage_transitions,
stages,
execution_mode,
restart_execution_on_update,
triggers,
role_arn,
name,
variables,
version,
artifact_store,
pipeline_type,
tag_key,
tag_value
FROM aws.codepipeline.pipeline_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>pipeline_tags</code> resource, see <a href="/providers/aws/codepipeline/pipelines/#permissions"><code>pipelines</code></a>

