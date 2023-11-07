---
title: connector_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_profile
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
Gets an individual <code>connector_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connector_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connector_profile</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appflow.connector_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ConnectorProfileArn</code></td><td><code>string</code></td><td>Unique identifier for connector profile resources</td></tr>
<tr><td><code>ConnectorLabel</code></td><td><code>string</code></td><td>The label of the connector. The label is unique for each ConnectorRegistration in your AWS account. Only needed if calling for CUSTOMCONNECTOR connector type&#x2F;.</td></tr>
<tr><td><code>ConnectorProfileName</code></td><td><code>string</code></td><td>The maximum number of items to retrieve in a single batch.</td></tr>
<tr><td><code>KMSArn</code></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><code>ConnectorType</code></td><td><code>undefined</code></td><td>List of Saas providers that need connector profile to be created</td></tr>
<tr><td><code>ConnectionMode</code></td><td><code>string</code></td><td>Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular</td></tr>
<tr><td><code>ConnectorProfileConfig</code></td><td><code>undefined</code></td><td>Connector specific configurations needed to create connector profile</td></tr>
<tr><td><code>CredentialsArn</code></td><td><code>string</code></td><td>A unique Arn for Connector-Profile resource</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appflow.connector_profile
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ConnectorProfileName&gt;'
</pre>
