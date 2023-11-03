---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.transfer.connectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccessRole</code></td><td><code>string</code></td><td>Specifies the access role for the connector.</td></tr><tr><td><code>As2Config</code></td><td><code>object</code></td><td>Configuration for an AS2 connector.</td></tr><tr><td><code>Arn</code></td><td><code>string</code></td><td>Specifies the unique Amazon Resource Name (ARN) for the workflow.</td></tr><tr><td><code>ConnectorId</code></td><td><code>string</code></td><td>A unique identifier for the connector.</td></tr><tr><td><code>LoggingRole</code></td><td><code>string</code></td><td>Specifies the logging role for the connector.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.</td></tr><tr><td><code>Url</code></td><td><code>string</code></td><td>URL for Connector</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.transfer.connectors
WHERE region = 'us-east-1'
</pre>
