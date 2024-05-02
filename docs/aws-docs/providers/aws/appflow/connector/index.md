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
Gets or operates on an individual <code>connector</code> resource, use <code>connectors</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AppFlow::Connector</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appflow.connector</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
connector_label,
connector_arn,
connector_provisioning_type,
connector_provisioning_config,
description
FROM aws.appflow.connector
WHERE data__Identifier = '<ConnectorLabel>';
```

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

