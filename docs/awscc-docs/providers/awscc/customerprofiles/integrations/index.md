---
title: integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - integrations
  - customerprofiles
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>integrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integrations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.customerprofiles.integrations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><code>uri</code></td><td><code>string</code></td><td>The URI of the S3 bucket or any other type of data source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>integrations</code> resource, the following permissions are required:

### Create
<pre>
profile:GetIntegration,
profile:PutIntegration,
appflow:CreateFlow,
app-integrations:CreateEventIntegrationAssociation,
app-integrations:GetEventIntegration,
events:ListTargetsByRule,
events:PutRule,
events:PutTargets,
events:PutEvents,
profile:TagResource</pre>

### List
<pre>
profile:ListIntegrations</pre>


## Example
```sql
SELECT
region,
domain_name,
uri
FROM awscc.customerprofiles.integrations
WHERE region = 'us-east-1'
```
