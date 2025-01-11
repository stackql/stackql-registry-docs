---
title: resource_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_configurations
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

Creates, updates, deletes or gets a <code>resource_configuration</code> resource or lists <code>resource_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>VpcLattice ResourceConfiguration CFN resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.resource_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allow_association_to_sharable_service_network" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="protocol_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_configuration_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="port_ranges" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_configuration_definition" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_configuration_auth_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="resource_configuration_group_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-resourceconfiguration.html"><code>AWS::VpcLattice::ResourceConfiguration</code></a>.

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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>resource_configurations</code> in a region.
```sql
SELECT
region,
allow_association_to_sharable_service_network,
protocol_type,
resource_configuration_type,
port_ranges,
resource_configuration_definition,
id,
resource_gateway_id,
arn,
resource_configuration_auth_type,
resource_configuration_group_id,
tags,
name
FROM aws.vpclattice.resource_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_configuration</code>.
```sql
SELECT
region,
allow_association_to_sharable_service_network,
protocol_type,
resource_configuration_type,
port_ranges,
resource_configuration_definition,
id,
resource_gateway_id,
arn,
resource_configuration_auth_type,
resource_configuration_group_id,
tags,
name
FROM aws.vpclattice.resource_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.vpclattice.resource_configurations (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.resource_configurations (
 AllowAssociationToSharableServiceNetwork,
 ProtocolType,
 ResourceConfigurationType,
 PortRanges,
 ResourceConfigurationDefinition,
 ResourceGatewayId,
 ResourceConfigurationAuthType,
 ResourceConfigurationGroupId,
 Tags,
 Name,
 region
)
SELECT 
 '{{ AllowAssociationToSharableServiceNetwork }}',
 '{{ ProtocolType }}',
 '{{ ResourceConfigurationType }}',
 '{{ PortRanges }}',
 '{{ ResourceConfigurationDefinition }}',
 '{{ ResourceGatewayId }}',
 '{{ ResourceConfigurationAuthType }}',
 '{{ ResourceConfigurationGroupId }}',
 '{{ Tags }}',
 '{{ Name }}',
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
  - name: resource_configuration
    props:
      - name: AllowAssociationToSharableServiceNetwork
        value: '{{ AllowAssociationToSharableServiceNetwork }}'
      - name: ProtocolType
        value: '{{ ProtocolType }}'
      - name: ResourceConfigurationType
        value: '{{ ResourceConfigurationType }}'
      - name: PortRanges
        value:
          - '{{ PortRanges[0] }}'
      - name: ResourceConfigurationDefinition
        value: {}
      - name: ResourceGatewayId
        value: '{{ ResourceGatewayId }}'
      - name: ResourceConfigurationAuthType
        value: '{{ ResourceConfigurationAuthType }}'
      - name: ResourceConfigurationGroupId
        value: '{{ ResourceConfigurationGroupId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Name
        value: '{{ Name }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.vpclattice.resource_configurations
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_configurations</code> resource, the following permissions are required:

### Read
```json
vpc-lattice:GetResourceConfiguration,
vpc-lattice:ListTagsForResource
```

### Create
```json
ec2:DescribeSubnets,
vpc-lattice:CreateResourceConfiguration,
vpc-lattice:GetResourceConfiguration,
vpc-lattice:TagResource,
vpc-lattice:ListTagsForResource
```

### Update
```json
ec2:DescribeSubnets,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:ListTagsForResource,
vpc-lattice:UpdateResourceConfiguration,
vpc-lattice:GetResourceConfiguration
```

### List
```json
vpc-lattice:ListResourceConfigurations
```

### Delete
```json
vpc-lattice:DeleteResourceConfiguration,
vpc-lattice:GetResourceConfiguration,
vpc-lattice:UntagResource
```
