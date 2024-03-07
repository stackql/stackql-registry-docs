---
title: service_action_association
hide_title: false
hide_table_of_contents: false
keywords:
  - service_action_association
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
Gets an individual <code>service_action_association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_action_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>service_action_association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.servicecatalog.service_action_association</code></td></tr>
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

## Example
```sql
SELECT
region,
product_id,
provisioning_artifact_id,
service_action_id
FROM awscc.servicecatalog.service_action_association
WHERE region = 'us-east-1'
AND data__Identifier = '{ProductId}';
AND data__Identifier = '{ProvisioningArtifactId}';
AND data__Identifier = '{ServiceActionId}';
```

## Permissions

To operate on the <code>service_action_association</code> resource, the following permissions are required:

### Read
```json
servicecatalog:ListServiceActionsForProvisioningArtifact
```

### Delete
```json
servicecatalog:DisassociateServiceActionFromProvisioningArtifact,
servicecatalog:ListServiceActionsForProvisioningArtifact
```

