---
title: service_network_resource_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - service_network_resource_associations
  - vpclattice
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

Creates, updates, deletes or gets a <code>service_network_resource_association</code> resource or lists <code>service_network_resource_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_network_resource_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>VpcLattice ServiceNetworkResourceAssociation CFN resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.service_network_resource_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_configuration_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_network_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetworkresourceassociation.html"><code>AWS::VpcLattice::ServiceNetworkResourceAssociation</code></a>.

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
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>service_network_resource_associations</code> in a region.
```sql
SELECT
region,
id,
arn,
resource_configuration_id,
service_network_id,
tags
FROM aws.vpclattice.service_network_resource_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>service_network_resource_association</code>.
```sql
SELECT
region,
id,
arn,
resource_configuration_id,
service_network_id,
tags
FROM aws.vpclattice.service_network_resource_associations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_network_resource_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
INSERT INTO aws.vpclattice.service_network_resource_associations (
 ResourceConfigurationId,
 ServiceNetworkId,
 Tags,
 region
)
SELECT 
'{{ ResourceConfigurationId }}',
 '{{ ServiceNetworkId }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.service_network_resource_associations (
 ResourceConfigurationId,
 ServiceNetworkId,
 Tags,
 region
)
SELECT 
 '{{ ResourceConfigurationId }}',
 '{{ ServiceNetworkId }}',
 '{{ Tags }}',
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
  - name: service_network_resource_association
    props:
      - name: ResourceConfigurationId
        value: '{{ ResourceConfigurationId }}'
      - name: ServiceNetworkId
        value: '{{ ServiceNetworkId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.vpclattice.service_network_resource_associations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_network_resource_associations</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:CreateServiceNetworkResourceAssociation,
vpc-lattice:GetServiceNetworkResourceAssociation,
vpc-lattice:TagResource,
vpc-lattice:ListTagsForResource
```

### Read
```json
vpc-lattice:GetServiceNetworkResourceAssociation,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:GetServiceNetworkResourceAssociation,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteServiceNetworkResourceAssociation,
vpc-lattice:GetServiceNetworkResourceAssociation,
vpc-lattice:UntagResource
```

### List
```json
vpc-lattice:ListServiceNetworkResourceAssociations
```
