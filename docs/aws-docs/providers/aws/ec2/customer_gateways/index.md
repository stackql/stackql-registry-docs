---
title: customer_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_gateways
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

Creates, updates, deletes or gets a <code>customer_gateway</code> resource or lists <code>customer_gateways</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a customer gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.customer_gateways" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of VPN connection that this customer gateway supports (<code>ipsec.1</code>).</td></tr>
<tr><td><CopyableCode code="customer_gateway_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="ip_address" /></td><td><code>string</code></td><td>IPv4 address for the customer gateway device's outside interface. The address must be static.</td></tr>
<tr><td><CopyableCode code="bgp_asn_extended" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="bgp_asn" /></td><td><code>integer</code></td><td>For devices that support BGP, the customer gateway's BGP ASN.<br />Default: 65000</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags for the customer gateway.</td></tr>
<tr><td><CopyableCode code="certificate_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="device_name" /></td><td><code>string</code></td><td>The name of customer gateway device.</td></tr>
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
    <td><CopyableCode code="IpAddress, Type, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>customer_gateways</code> in a region.
```sql
SELECT
region,
customer_gateway_id
FROM aws.ec2.customer_gateways
WHERE region = 'us-east-1';
```
Gets all properties from a <code>customer_gateway</code>.
```sql
SELECT
region,
type,
customer_gateway_id,
ip_address,
bgp_asn_extended,
bgp_asn,
tags,
certificate_arn,
device_name
FROM aws.ec2.customer_gateways
WHERE region = 'us-east-1' AND data__Identifier = '<CustomerGatewayId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>customer_gateway</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ec2.customer_gateways (
 Type,
 IpAddress,
 region
)
SELECT 
'{{ Type }}',
 '{{ IpAddress }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ec2.customer_gateways (
 Type,
 IpAddress,
 BgpAsnExtended,
 BgpAsn,
 Tags,
 CertificateArn,
 DeviceName,
 region
)
SELECT 
 '{{ Type }}',
 '{{ IpAddress }}',
 '{{ BgpAsnExtended }}',
 '{{ BgpAsn }}',
 '{{ Tags }}',
 '{{ CertificateArn }}',
 '{{ DeviceName }}',
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
  - name: customer_gateway
    props:
      - name: Type
        value: '{{ Type }}'
      - name: IpAddress
        value: '{{ IpAddress }}'
      - name: BgpAsnExtended
        value: null
      - name: BgpAsn
        value: '{{ BgpAsn }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CertificateArn
        value: '{{ CertificateArn }}'
      - name: DeviceName
        value: '{{ DeviceName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ec2.customer_gateways
WHERE data__Identifier = '<CustomerGatewayId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>customer_gateways</code> resource, the following permissions are required:

### Read
```json
ec2:DescribeCustomerGateways
```

### Create
```json
ec2:CreateCustomerGateway,
ec2:DescribeCustomerGateways,
ec2:CreateTags
```

### Update
```json
ec2:CreateTags,
ec2:DeleteTags,
ec2:DescribeCustomerGateways
```

### List
```json
ec2:DescribeCustomerGateways
```

### Delete
```json
ec2:DeleteCustomerGateway,
ec2:DescribeCustomerGateways,
ec2:DeleteTags
```

