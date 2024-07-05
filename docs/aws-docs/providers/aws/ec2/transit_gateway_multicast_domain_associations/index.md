---
title: transit_gateway_multicast_domain_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - transit_gateway_multicast_domain_associations
  - ec2
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

Creates, updates, deletes or gets a <code>transit_gateway_multicast_domain_association</code> resource or lists <code>transit_gateway_multicast_domain_associations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transit_gateway_multicast_domain_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::TransitGatewayMulticastDomainAssociation type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.transit_gateway_multicast_domain_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="transit_gateway_multicast_domain_id" /></td><td><code>string</code></td><td>The ID of the transit gateway multicast domain.</td></tr>
<tr><td><CopyableCode code="transit_gateway_attachment_id" /></td><td><code>string</code></td><td>The ID of the transit gateway attachment.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The ID of the resource.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The type of resource, for example a VPC attachment.</td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td>The state of the subnet association.</td></tr>
<tr><td><CopyableCode code="subnet_id" /></td><td><code>string</code></td><td>The IDs of the subnets to associate with the transit gateway multicast domain.</td></tr>
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
    <td><CopyableCode code="TransitGatewayMulticastDomainId, TransitGatewayAttachmentId, SubnetId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>transit_gateway_multicast_domain_associations</code> in a region.
```sql
SELECT
region,
transit_gateway_multicast_domain_id,
transit_gateway_attachment_id,
resource_id,
resource_type,
state,
subnet_id
FROM aws.ec2.transit_gateway_multicast_domain_associations
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>transit_gateway_multicast_domain_association</code>.
```sql
SELECT
region,
transit_gateway_multicast_domain_id,
transit_gateway_attachment_id,
resource_id,
resource_type,
state,
subnet_id
FROM aws.ec2.transit_gateway_multicast_domain_associations
WHERE region = 'us-east-1' AND data__Identifier = '<TransitGatewayMulticastDomainId>|<TransitGatewayAttachmentId>|<SubnetId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transit_gateway_multicast_domain_association</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.transit_gateway_multicast_domain_associations (
 TransitGatewayMulticastDomainId,
 TransitGatewayAttachmentId,
 SubnetId,
 region
)
SELECT 
'{{ TransitGatewayMulticastDomainId }}',
 '{{ TransitGatewayAttachmentId }}',
 '{{ SubnetId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.transit_gateway_multicast_domain_associations (
 TransitGatewayMulticastDomainId,
 TransitGatewayAttachmentId,
 SubnetId,
 region
)
SELECT 
 '{{ TransitGatewayMulticastDomainId }}',
 '{{ TransitGatewayAttachmentId }}',
 '{{ SubnetId }}',
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
  - name: transit_gateway_multicast_domain_association
    props:
      - name: TransitGatewayMulticastDomainId
        value: '{{ TransitGatewayMulticastDomainId }}'
      - name: TransitGatewayAttachmentId
        value: '{{ TransitGatewayAttachmentId }}'
      - name: SubnetId
        value: '{{ SubnetId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.transit_gateway_multicast_domain_associations
WHERE data__Identifier = '<TransitGatewayMulticastDomainId|TransitGatewayAttachmentId|SubnetId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>transit_gateway_multicast_domain_associations</code> resource, the following permissions are required:

### Create
```json
ec2:AssociateTransitGatewayMulticastDomain,
ec2:GetTransitGatewayMulticastDomainAssociations
```

### Read
```json
ec2:GetTransitGatewayMulticastDomainAssociations
```

### Delete
```json
ec2:DisassociateTransitGatewayMulticastDomain,
ec2:GetTransitGatewayMulticastDomainAssociations
```

### List
```json
ec2:GetTransitGatewayMulticastDomainAssociations
```

