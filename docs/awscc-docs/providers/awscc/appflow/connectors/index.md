---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
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
Retrieves a list of <code>connectors</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connectors</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appflow.connectors</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connector_label</code></td><td><code>string</code></td><td> The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
connector_label
FROM awscc.appflow.connectors
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>connectors</code> resource, the following permissions are required:

### Create
```json
appflow:RegisterConnector,
lambda:InvokeFunction
```

### List
```json
appflow:ListConnectors
```

