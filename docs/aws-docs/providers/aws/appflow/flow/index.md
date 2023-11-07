---
title: flow
hide_title: false
hide_table_of_contents: false
keywords:
  - flow
  - appflow
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flow</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appflow.flow</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FlowArn</code></td><td><code>string</code></td><td>ARN identifier of the flow.</td></tr>
<tr><td><code>FlowName</code></td><td><code>string</code></td><td>Name of the flow.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Description of the flow.</td></tr>
<tr><td><code>KMSArn</code></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><code>TriggerConfig</code></td><td><code>object</code></td><td>Trigger settings of the flow.</td></tr>
<tr><td><code>SourceFlowConfig</code></td><td><code>object</code></td><td>Configurations of Source connector of the flow.</td></tr>
<tr><td><code>DestinationFlowConfigList</code></td><td><code>array</code></td><td>List of Destination connectors of the flow.</td></tr>
<tr><td><code>Tasks</code></td><td><code>array</code></td><td>List of tasks for the flow.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>List of Tags.</td></tr>
<tr><td><code>MetadataCatalogConfig</code></td><td><code>object</code></td><td>Configurations of metadata catalog of the flow.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appflow.flow<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;FlowName&gt;'
</pre>
