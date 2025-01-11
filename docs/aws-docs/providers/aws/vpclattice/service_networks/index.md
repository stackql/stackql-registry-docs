---
title: service_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - service_networks
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

Creates, updates, deletes or gets a <code>service_network</code> resource or lists <code>service_networks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A service network is a logical boundary for a collection of services. You can associate services and VPCs with a service network.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.vpclattice.service_networks" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="sharing_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-vpclattice-servicenetwork.html"><code>AWS::VpcLattice::ServiceNetwork</code></a>.

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
Gets all <code>service_networks</code> in a region.
```sql
SELECT
region,
arn,
created_at,
id,
last_updated_at,
name,
auth_type,
tags,
sharing_config
FROM aws.vpclattice.service_networks
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>service_network</code>.
```sql
SELECT
region,
arn,
created_at,
id,
last_updated_at,
name,
auth_type,
tags,
sharing_config
FROM aws.vpclattice.service_networks
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_network</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.vpclattice.service_networks (
 Name,
 AuthType,
 Tags,
 SharingConfig,
 region
)
SELECT 
'{{ Name }}',
 '{{ AuthType }}',
 '{{ Tags }}',
 '{{ SharingConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.vpclattice.service_networks (
 Name,
 AuthType,
 Tags,
 SharingConfig,
 region
)
SELECT 
 '{{ Name }}',
 '{{ AuthType }}',
 '{{ Tags }}',
 '{{ SharingConfig }}',
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
  - name: service_network
    props:
      - name: Name
        value: '{{ Name }}'
      - name: AuthType
        value: '{{ AuthType }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: SharingConfig
        value:
          enabled: '{{ enabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.vpclattice.service_networks
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>service_networks</code> resource, the following permissions are required:

### Create
```json
vpc-lattice:GetServiceNetwork,
vpc-lattice:ListTagsForResource,
vpc-lattice:CreateServiceNetwork,
vpc-lattice:TagResource,
iam:CreateServiceLinkedRole
```

### Read
```json
vpc-lattice:GetServiceNetwork,
vpc-lattice:ListTagsForResource
```

### Update
```json
vpc-lattice:GetServiceNetwork,
vpc-lattice:UpdateServiceNetwork,
vpc-lattice:TagResource,
vpc-lattice:UntagResource,
vpc-lattice:ListTagsForResource
```

### Delete
```json
vpc-lattice:DeleteServiceNetwork,
vpc-lattice:UntagResource
```

### List
```json
vpc-lattice:ListServiceNetworks
```
