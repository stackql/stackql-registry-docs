---
title: service_principal_names
hide_title: false
hide_table_of_contents: false
keywords:
  - service_principal_names
  - pcaconnectorad
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>service_principal_names</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principal_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_principal_names</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.pcaconnectorad.service_principal_names</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>connector_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>directory_registration_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>service_principal_names</code> resource, the following permissions are required:

### Create
<pre>
ds:UpdateAuthorizedApplication,
pca-connector-ad:GetServicePrincipalName,
pca-connector-ad:CreateServicePrincipalName</pre>

### List
<pre>
pca-connector-ad:ListServicePrincipalNames</pre>


## Example
```sql
SELECT
region,
connector_arn,
directory_registration_arn
FROM awscc.pcaconnectorad.service_principal_names
WHERE region = 'us-east-1'
```
