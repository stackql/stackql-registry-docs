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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>service_action_associations</code> in a region or to create or delete a <code>service_action_associations</code> resource, use <code>service_action_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_action_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Schema for AWS::ServiceCatalog::ServiceActionAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.servicecatalog.service_action_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="product_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_artifact_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_action_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
product_id,
provisioning_artifact_id,
service_action_id
FROM aws.servicecatalog.service_action_associations
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>service_action_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
-- service_action_association.iql (required properties only)
INSERT INTO aws.servicecatalog.service_action_associations (
 ProductId,
 ProvisioningArtifactId,
 ServiceActionId,
 region
)
SELECT 
'{{ ProductId }}',
 '{{ ProvisioningArtifactId }}',
 '{{ ServiceActionId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- service_action_association.iql (all properties)
INSERT INTO aws.servicecatalog.service_action_associations (
 ProductId,
 ProvisioningArtifactId,
 ServiceActionId,
 region
)
SELECT 
 '{{ ProductId }}',
 '{{ ProvisioningArtifactId }}',
 '{{ ServiceActionId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: service_action_association
    props:
      - name: ProductId
        value: '{{ ProductId }}'
      - name: ProvisioningArtifactId
        value: '{{ ProvisioningArtifactId }}'
      - name: ServiceActionId
        value: '{{ ServiceActionId }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.servicecatalog.service_action_associations
WHERE data__Identifier = '<ProductId|ProvisioningArtifactId|ServiceActionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_action_associations</code> resource, the following permissions are required:

### Create
```json
servicecatalog:AssociateServiceActionWithProvisioningArtifact,
servicecatalog:ListServiceActionsForProvisioningArtifact
```

### Delete
```json
servicecatalog:DisassociateServiceActionFromProvisioningArtifact,
servicecatalog:ListServiceActionsForProvisioningArtifact
```

### List
```json
servicecatalog:ListServiceActionsForProvisioningArtifact
```

