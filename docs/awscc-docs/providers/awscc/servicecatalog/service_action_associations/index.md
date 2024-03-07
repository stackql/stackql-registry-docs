---
title: service_action_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_action_associations
  - servicecatalog
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>service_action_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_action_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_action_associations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.servicecatalog.service_action_associations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>product_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>provisioning_artifact_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>service_action_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>service_action_associations</code> resource, the following permissions are required:

### Create
<pre>
servicecatalog:AssociateServiceActionWithProvisioningArtifact,
servicecatalog:ListServiceActionsForProvisioningArtifact</pre>

### List
<pre>
servicecatalog:ListServiceActionsForProvisioningArtifact</pre>


## Example
```sql
SELECT
region,
product_id,
provisioning_artifact_id,
service_action_id
FROM awscc.servicecatalog.service_action_associations
WHERE region = 'us-east-1'
```
