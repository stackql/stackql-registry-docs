---
title: connector
hide_title: false
hide_table_of_contents: false
keywords:
  - connector
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
Gets an individual <code>connector</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connector</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.appflow.connector</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connector_label</code></td><td><code>string</code></td><td> The name of the connector. The name is unique for each ConnectorRegistration in your AWS account.</td></tr>
<tr><td><code>connector_arn</code></td><td><code>string</code></td><td> The arn of the connector. The arn is unique for each ConnectorRegistration in your AWS account.</td></tr>
<tr><td><code>connector_provisioning_type</code></td><td><code>string</code></td><td>The provisioning type of the connector. Currently the only supported value is LAMBDA. </td></tr>
<tr><td><code>connector_provisioning_config</code></td><td><code>object</code></td><td>Contains information about the configuration of the connector being registered.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description about the connector that's being registered.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>connector</code> resource, the following permissions are required:

### Read
```json
appflow:DescribeConnector
```

### Delete
```json
appflow:UnRegisterConnector
```

### Update
```json
appflow:UpdateConnectorRegistration,
lambda:InvokeFunction
```


## Example
```sql
SELECT
region,
connector_label,
connector_arn,
connector_provisioning_type,
connector_provisioning_config,
description
FROM awscc.appflow.connector
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ConnectorLabel&gt;'
```
