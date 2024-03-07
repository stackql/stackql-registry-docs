---
title: integration
hide_title: false
hide_table_of_contents: false
keywords:
  - integration
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
Gets an individual <code>integration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>integration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.customerprofiles.integration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>domain_name</code></td><td><code>string</code></td><td>The unique name of the domain.</td></tr>
<tr><td><code>uri</code></td><td><code>string</code></td><td>The URI of the S3 bucket or any other type of data source.</td></tr>
<tr><td><code>flow_definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>object_type_name</code></td><td><code>string</code></td><td>The name of the ObjectType defined for the 3rd party data in Profile Service</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The time of this integration got created</td></tr>
<tr><td><code>last_updated_at</code></td><td><code>string</code></td><td>The time of this integration got last updated at</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags (keys and values) associated with the integration</td></tr>
<tr><td><code>object_type_names</code></td><td><code>array</code></td><td>The mapping between 3rd party event types and ObjectType names</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>integration</code> resource, the following permissions are required:

### Read
<pre>
profile:GetIntegration</pre>

### Delete
<pre>
profile:DeleteIntegration,
appflow:DeleteFlow,
app-integrations:ListEventIntegrationAssociations,
app-integrations:DeleteEventIntegrationAssociation,
events:RemoveTargets,
events:ListTargetsByRule,
events:DeleteRule</pre>

### Update
<pre>
profile:PutIntegration,
profile:GetIntegration,
appflow:CreateFlow,
app-integrations:GetEventIntegration,
app-integrations:CreateEventIntegrationAssociation,
app-integrations:ListEventIntegrationAssociations,
app-integrations:DeleteEventIntegrationAssociation,
events:ListTargetsByRule,
events:RemoveTargets,
events:DeleteRule,
events:PutRule,
events:PutTargets,
events:PutEvents,
profile:UntagResource,
profile:TagResource</pre>


## Example
```sql
SELECT
region,
domain_name,
uri,
flow_definition,
object_type_name,
created_at,
last_updated_at,
tags,
object_type_names
FROM awscc.customerprofiles.integration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DomainName&gt;'
AND data__Identifier = '&lt;Uri&gt;'
```
